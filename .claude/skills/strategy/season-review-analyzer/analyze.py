import sys
import os
from typing import List, Dict

# 현재 스크립트의 위치를 path에 추가하여 동료 모듈 import 보장
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import SALES_DATA, VOC_DATA, MARKETING_DATA

class SeasonReviewAgent:
    def __init__(self):
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze_complex_data(self):
        results = []
        
        for item in SALES_DATA:
            sku = item['sku']
            
            # 1. Basic Quant
            sold_qty = item['sold_qty']
            return_qty = item.get('return_qty', 0)
            net_sales_qty = sold_qty - return_qty
            
            initial_stock = item['initial_stock']
            gross_sell_through = (sold_qty / initial_stock) * 100
            net_sell_through = (net_sales_qty / initial_stock) * 100
            return_rate = (return_qty / sold_qty * 100) if sold_qty > 0 else 0
            
            # 2. Marketing Data Match
            mkt_data = next((m for m in MARKETING_DATA if m['sku'] == sku), None)
            roas = 0.0
            if mkt_data:
                revenue = net_sales_qty * item['price']
                ad_spend = mkt_data['ad_spend']
                roas = (revenue / ad_spend * 100) if ad_spend > 0 else 0
            
            # 3. Decision Logic (Strategy)
            status = "MAINTAIN"
            action_plan = ""
            
            # Case A: High Return (Fit/Qual Issue)
            if return_rate >= 20:
                status = "REVAMP" # 전면 수정 필요
                major_reason = max(item['return_reason'], key=item['return_reason'].get)
                action_plan = f"**[구조개선]** 반품률 {return_rate:.1f}% (주원인: {major_reason}). 패턴/스펙 전면 수정."
            
            # Case B: High Sales, Low Return (Best Seller)
            elif net_sell_through >= 80:
                status = "EXPAND"
                action_plan = "**[확대]** 검증된 베스트셀러. 물량 2배 증대 및 리오더 시스템 구축."
            
            # Case C: Low Sales but High Quality (Hidden Gem)
            elif net_sell_through <= 40 and return_rate < 5:
                status = "BOOST" # 마케팅 강화 필요
                action_plan = "**[마케팅 투자]** 반품률 최저({return_rate:.1f}%). 제품력 우수하나 노출 부족. 광고 예산 3배 증액."
                
            # Case D: Low Sales, Low Quality
            elif net_sell_through <= 40 and return_rate >= 10:
                status = "DROP"
                action_plan = "**[단종]** 시장 반응 냉담 & 품질 이슈. 즉시 드랍."

            results.append({
                "sku": sku,
                "name": item['name'],
                "net_sell_through": round(net_sell_through, 1),
                "return_rate": round(return_rate, 1),
                "roas": round(roas, 0) if mkt_data else "N/A",
                "status": status,
                "action_plan": action_plan
            })
            
        return results

    def analyze_qual_issues(self) -> Dict[str, List[str]]:
        issues = {}
        for voc in VOC_DATA:
            # 긍정적이어도 개선점 있으면 수집하지만, 일단 부정 리뷰 위주
            if voc['sentiment'] == 'negative':
                sku = voc['sku']
                if sku not in issues:
                    issues[sku] = []
                issues[sku].append(voc['comment'])
        return issues

    def generate_strategy(self):
        print("🔍 [Agent] 고도화된 시즌 리뷰 분석 시작 (Quant + Qual + Return + Marketing)...")
        
        quant_results = self.analyze_complex_data()
        qual_issues = self.analyze_qual_issues()

        # 1. Generate OTB Plan (Strategy)
        strategy_md = "# 26SS 상품운영계획서 (Merchandising Plan V2)\n\n"
        strategy_md += "## 📊 카테고리별 성과 분석\n"
        strategy_md += "| SKU | 상품명 | 실판매율(%) | 반품률(%) | ROAS | 판정 | 26SS 전략 |\n"
        strategy_md += "|---|---|---|---|---|---|---|\n"

        for res in quant_results:
            strategy_md += f"| {res['sku']} | {res['name']} | {res['net_sell_through']}% | **{res['return_rate']}%** | {res['roas']}% | {res['status']} | {res['action_plan']} |\n"
        
        with open(f"{self.output_dir}/Season_Strategy.md", "w") as f:
            f.write(strategy_md)
            
        print(f"✅ [Agent] 전략 문서 생성 완료: {self.output_dir}/Season_Strategy.md")

        # 2. Generate Product Dev Request (Design)
        dev_req_md = "# 26SS 상품개발의뢰서 (Product Dev Request V2)\n\n"
        dev_req_md += "## 🚨 긴급 개선 요망 (Pain Points)\n"
        
        for res in quant_results:
            if res['status'] == "REVAMP": # 반품률 높은 상품 집중 케어
                sku = res['sku']
                voc_list = qual_issues.get(sku, [])
                
                dev_req_md += f"### {res['name']} ({sku})\n"
                dev_req_md += f"**⚠️ Critical Issue:** 반품률 {res['return_rate']}% (마케팅 성공했으나 제품력 실패)\n"
                dev_req_md += "**VOC 불만 사항:**\n"
                for comment in voc_list:
                    dev_req_md += f"- \"{comment}\"\n"
                
                dev_req_md += "\n**🛠 개발 지침 (Action Item):**\n"
                dev_req_md += "- **[Fit Revision]** 기장 스펙 전면 수정 (-5cm ~ -7cm). 한국인 표준 체형 데이터 반영.\n"
                dev_req_md += "- **[Detail]** 밑단 컷팅 방식 변경으로 수선 용이성 확보.\n"
                dev_req_md += "\n---\n"
                
            elif res['status'] == "BOOST": # 숨은 보석
                 dev_req_md += f"### {res['name']} ({res['sku']})\n"
                 dev_req_md += f"**💎 Hidden Gem:** 반품률 {res['return_rate']}% (극강의 만족도)\n"
                 dev_req_md += "**🛠 개발 지침 (Action Item):**\n"
                 dev_req_md += "- **[Variation]** 스펙 100% 유지하되 컬러 베리에이션 5종 추가.\n"
                 dev_req_md += "- **[Carry-over]** 시그니처 아이템으로 지정하여 영구 결번(No Sale).\n"
                 dev_req_md += "\n---\n"

        with open(f"{self.output_dir}/Product_Dev_Request.md", "w") as f:
            f.write(dev_req_md)

        print(f"✅ [Agent] 개발 의뢰서 생성 완료: {self.output_dir}/Product_Dev_Request.md")

if __name__ == "__main__":
    agent = SeasonReviewAgent()
    agent.generate_strategy()
