#!/usr/bin/env python3
"""
Sales Analyzer - 주간/월간 판매 데이터 분석 스크립트
Usage: python analyze_sales.py <file_path> [brand]
"""

import pandas as pd
import sys
from datetime import datetime
from pathlib import Path

# 브랜드별 컬럼 매핑
BRAND_COLUMNS = {
    '커버낫': {'start': 4, 'end': 14},
    '와키윌리': {'start': 18, 'end': 28},
    '리(LEE)': {'start': 32, 'end': 42}
}

# 카테고리 분류 키워드
CATEGORIES = {
    '아우터(다운/점퍼)': ['다운', '점퍼', '자켓', '코트', '푸퍼', '패딩', '플리스'],
    '상의(후드/맨투맨)': ['후드', '맨투맨', '스웻', '티셔츠', '니트', '하프집업'],
    '하의(팬츠)': ['팬츠', '조거', '진', '쇼츠', '숏팬츠'],
    '액세서리': ['모자', '가방', '양말', '머플러']
}

def load_data(file_path: str) -> pd.DataFrame:
    """엑셀 파일 로드"""
    return pd.read_excel(file_path, sheet_name='BEST 10_WB', header=None)

def get_brand_summary(df: pd.DataFrame) -> dict:
    """브랜드별 기간 매출 요약"""
    summary = {}
    for brand, cols in BRAND_COLUMNS.items():
        sales = df.iloc[5, cols['start']]
        if pd.notna(sales):
            summary[brand] = {'매출': float(sales), 'start': cols['start']}
    total = sum(b['매출'] for b in summary.values())
    for brand in summary:
        summary[brand]['점유율'] = summary[brand]['매출'] / total * 100
    return summary

def get_best10_products(df: pd.DataFrame, brand: str) -> list:
    """BEST 10 상품 추출"""
    if brand not in BRAND_COLUMNS:
        return []

    start = BRAND_COLUMNS[brand]['start']
    products = []

    for i in range(10):
        col = start + i
        product = {
            '순위': i + 1,
            '품번': df.iloc[8, col],
            '품명': df.iloc[9, col],
            'TAG가': df.iloc[10, col],
            '판매수량': df.iloc[11, col],
            'TAG금액': df.iloc[12, col],
            '판매금액': df.iloc[13, col],
            '온라인': df.iloc[14, col],
            '오프라인': df.iloc[15, col],
            '면세': df.iloc[16, col],
            '기타': df.iloc[17, col],
            '매출비중': df.iloc[18, col],
            '전주금액': df.iloc[19, col],
            '전주대비': df.iloc[20, col],
            '전주순위': df.iloc[21, col],
            '랭킹증감': df.iloc[22, col],
            '전체할인율': df.iloc[23, col],
            '정상할인율': df.iloc[24, col]
        }
        products.append(product)
    return products

def classify_category(product_name: str) -> str:
    """상품명으로 카테고리 분류"""
    if pd.isna(product_name):
        return '기타'
    for category, keywords in CATEGORIES.items():
        if any(kw in str(product_name) for kw in keywords):
            return category
    return '기타'

def analyze_channels(products: list) -> dict:
    """채널별 매출 분석"""
    total = sum(p['판매금액'] for p in products if pd.notna(p['판매금액']))
    online = sum(p['온라인'] for p in products if pd.notna(p['온라인']))
    offline = sum(p['오프라인'] for p in products if pd.notna(p['오프라인']))
    dutyfree = sum(p['면세'] for p in products if pd.notna(p['면세']))

    return {
        '총판매금액': total,
        '온라인': {'금액': online, '비중': online/total*100 if total > 0 else 0},
        '오프라인': {'금액': offline, '비중': offline/total*100 if total > 0 else 0},
        '면세': {'금액': dutyfree, '비중': dutyfree/total*100 if total > 0 else 0}
    }

def analyze_categories(products: list) -> dict:
    """카테고리별 분석"""
    categories = {}
    for p in products:
        cat = classify_category(p['품명'])
        if cat not in categories:
            categories[cat] = {'판매금액': 0, '판매수량': 0, '상품목록': []}
        if pd.notna(p['판매금액']):
            categories[cat]['판매금액'] += p['판매금액']
        if pd.notna(p['판매수량']):
            categories[cat]['판매수량'] += p['판매수량']
        categories[cat]['상품목록'].append(p['품명'])

    total = sum(c['판매금액'] for c in categories.values())
    for cat in categories:
        categories[cat]['비중'] = categories[cat]['판매금액']/total*100 if total > 0 else 0
    return categories

def analyze_growth(products: list) -> dict:
    """성장/하락 상품 분석"""
    growth = []
    decline = []

    for p in products:
        wow = p['전주대비']
        if pd.notna(wow):
            item = {'품명': p['품명'], '전주대비': wow * 100}
            if wow > 0:
                growth.append(item)
            elif wow < 0:
                decline.append(item)

    growth.sort(key=lambda x: x['전주대비'], reverse=True)
    decline.sort(key=lambda x: x['전주대비'])

    return {'성장': growth, '하락': decline}

def generate_insights(products: list, channels: dict, categories: dict, growth: dict) -> list:
    """전략적 인사이트 도출"""
    insights = []

    # 시즌 전환 감지
    outer_decline = sum(1 for p in growth['하락'] if any(kw in str(p['품명']) for kw in ['다운', '푸퍼', '패딩']))
    top_growth = sum(1 for p in growth['성장'] if any(kw in str(p['품명']) for kw in ['후드', '맨투맨', '스웻']))
    if outer_decline >= 2 and top_growth >= 2:
        insights.append("🔄 **시즌 전환 시점**: 다운류 하락, 경량 상의 상승 패턴 감지")

    # IP 상품 분석
    ip_growth = [p for p in growth['성장'] if any(kw in str(p['품명']) for kw in ['키키', '로고', 'KiKi'])]
    if len(ip_growth) >= 2:
        insights.append("🎭 **IP 인지도 상승**: 키키/로고 상품 다수 성장세")

    # 채널 분석
    if channels['온라인']['비중'] < 15:
        insights.append("📱 **온라인 채널 강화 필요**: 온라인 비중이 낮음 (업계 평균 대비)")
    if channels['면세']['비중'] > 15:
        insights.append("✈️ **인바운드 수요 활성화**: 면세 채널 매출 비중 양호")

    # 할인율 분석
    avg_discount = sum(p['전체할인율'] for p in products if pd.notna(p['전체할인율'])) / 10
    if avg_discount > 0.4:
        insights.append("⚠️ **마진 관리 주의**: 평균 할인율이 40%를 초과")
    elif avg_discount < 0.3:
        insights.append("✅ **브랜드 파워 양호**: 낮은 할인율로 판매 유지")

    return insights

def format_currency(value: float) -> str:
    """통화 포맷팅"""
    if pd.isna(value):
        return "-"
    if value >= 100000000:
        return f"{value/100000000:.1f}억원"
    elif value >= 10000:
        return f"{value/10000:.0f}만원"
    else:
        return f"{value:,.0f}원"

def generate_report(brand: str, summary: dict, products: list,
                   channels: dict, categories: dict, growth: dict, insights: list) -> str:
    """마크다운 보고서 생성"""
    report = []
    report.append(f"# {brand} 판매 분석 리포트")
    report.append(f"**분석일**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("")

    # 브랜드별 매출
    report.append("## 1. 브랜드별 매출 현황")
    report.append("| 브랜드 | 매출 | 점유율 |")
    report.append("|--------|------|--------|")
    for b, data in sorted(summary.items(), key=lambda x: x[1]['매출'], reverse=True):
        marker = "**" if b == brand else ""
        report.append(f"| {marker}{b}{marker} | {format_currency(data['매출'])} | {data['점유율']:.1f}% |")
    report.append("")

    # BEST 10
    report.append(f"## 2. {brand} BEST 10 상품")
    report.append("| 순위 | 품명 | TAG가 | 판매수량 | 판매금액 | 전주대비 |")
    report.append("|------|------|-------|---------|----------|----------|")
    for p in products:
        wow = f"+{p['전주대비']*100:.1f}%" if p['전주대비'] > 0 else f"{p['전주대비']*100:.1f}%"
        report.append(f"| {p['순위']} | {p['품명']} | ₩{p['TAG가']:,} | {p['판매수량']}개 | {format_currency(p['판매금액'])} | {wow} |")
    report.append("")

    # 채널별
    report.append("## 3. 채널별 매출")
    report.append(f"- **오프라인**: {format_currency(channels['오프라인']['금액'])} ({channels['오프라인']['비중']:.1f}%)")
    report.append(f"- **면세점**: {format_currency(channels['면세']['금액'])} ({channels['면세']['비중']:.1f}%)")
    report.append(f"- **온라인**: {format_currency(channels['온라인']['금액'])} ({channels['온라인']['비중']:.1f}%)")
    report.append("")

    # 카테고리별
    report.append("## 4. 카테고리별 분석")
    report.append("| 카테고리 | 매출 비중 | 판매수량 |")
    report.append("|----------|----------|----------|")
    for cat, data in sorted(categories.items(), key=lambda x: x[1]['판매금액'], reverse=True):
        report.append(f"| {cat} | {data['비중']:.1f}% | {int(data['판매수량'])}개 |")
    report.append("")

    # 성장/하락
    report.append("## 5. 전주 대비 변화")
    report.append("### 성장 상품")
    for item in growth['성장']:
        report.append(f"- 📈 {item['품명']}: **+{item['전주대비']:.1f}%**")
    report.append("")
    report.append("### 하락 상품")
    for item in growth['하락']:
        report.append(f"- 📉 {item['품명']}: {item['전주대비']:.1f}%")
    report.append("")

    # 인사이트
    report.append("## 6. 핵심 인사이트")
    for insight in insights:
        report.append(f"- {insight}")

    return "\n".join(report)

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_sales.py <file_path> [brand]")
        sys.exit(1)

    file_path = sys.argv[1]
    brand = sys.argv[2] if len(sys.argv) > 2 else '와키윌리'

    print(f"Loading data from: {file_path}")
    df = load_data(file_path)

    print("Analyzing brand summary...")
    summary = get_brand_summary(df)

    print(f"Extracting {brand} BEST 10...")
    products = get_best10_products(df, brand)

    print("Analyzing channels...")
    channels = analyze_channels(products)

    print("Analyzing categories...")
    categories = analyze_categories(products)

    print("Analyzing growth/decline...")
    growth = analyze_growth(products)

    print("Generating insights...")
    insights = generate_insights(products, channels, categories, growth)

    print("Generating report...")
    report = generate_report(brand, summary, products, channels, categories, growth, insights)

    # 보고서 출력
    print("\n" + "="*80 + "\n")
    print(report)

    # 파일로 저장
    output_dir = Path(file_path).parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"sales_report_{brand}_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n보고서 저장됨: {output_file}")

if __name__ == "__main__":
    main()
