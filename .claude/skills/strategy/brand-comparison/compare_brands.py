#!/usr/bin/env python3
"""
Brand Comparison Analyzer - 브랜드 비교 분석 스크립트
Usage: python compare_brands.py <file_path> [focus_brand]

Phase 1: 개별 브랜드 분석
Phase 2: 비교 분석 및 인사이트 도출
"""

import pandas as pd
import json
import sys
from datetime import datetime
from pathlib import Path

# 브랜드별 컬럼 매핑
BRAND_COLUMNS = {
    '커버낫': {'start': 4, 'sales_col': 4},
    '와키윌리': {'start': 18, 'sales_col': 18},
    '리(LEE)': {'start': 32, 'sales_col': 32}
}

CATEGORIES = {
    '아우터(다운/점퍼)': ['다운', '점퍼', '자켓', '코트', '푸퍼', '패딩', '플리스', '베스트', '더플'],
    '상의(후드/맨투맨)': ['후드', '맨투맨', '스웻', '하프집업', '집업'],
    '니트': ['니트'],
    '티셔츠': ['티셔츠', 'PACK'],
    '하의(팬츠)': ['팬츠', '조거', '진', '쇼츠'],
}

def safe_float(val):
    try:
        return float(val) if pd.notna(val) else 0
    except:
        return 0

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path, sheet_name='BEST 10_WB', header=None)

def analyze_single_brand(df: pd.DataFrame, brand: str) -> dict:
    """단일 브랜드 분석"""
    config = BRAND_COLUMNS[brand]
    start_col = config['start']

    # 기간 매출
    total_sales = safe_float(df.iloc[5, config['sales_col']])

    # BEST 10 상품 추출
    products = []
    for i in range(10):
        col = start_col + i
        products.append({
            '순위': i + 1,
            '품번': df.iloc[8, col],
            '품명': str(df.iloc[9, col]) if pd.notna(df.iloc[9, col]) else '',
            'TAG가': safe_float(df.iloc[10, col]),
            '판매수량': safe_float(df.iloc[11, col]),
            '판매금액': safe_float(df.iloc[13, col]),
            '온라인': safe_float(df.iloc[14, col]),
            '오프라인': safe_float(df.iloc[15, col]),
            '면세': safe_float(df.iloc[16, col]),
            '전주대비': safe_float(df.iloc[20, col]),
            '전체할인율': safe_float(df.iloc[23, col]),
        })

    # 채널별 합계
    best10_total = sum(p['판매금액'] for p in products)
    online = sum(p['온라인'] for p in products)
    offline = sum(p['오프라인'] for p in products)
    dutyfree = sum(p['면세'] for p in products)

    # 카테고리 분류
    categories = {}
    for p in products:
        cat = classify_category(p['품명'])
        if cat not in categories:
            categories[cat] = {'판매금액': 0, '판매수량': 0, '상품수': 0}
        categories[cat]['판매금액'] += p['판매금액']
        categories[cat]['판매수량'] += p['판매수량']
        categories[cat]['상품수'] += 1

    # 성장/하락 분류
    growth = [p for p in products if p['전주대비'] > 0]
    decline = [p for p in products if p['전주대비'] < 0]

    # 평균 지표
    avg_tag = sum(p['TAG가'] for p in products) / 10
    avg_discount = sum(p['전체할인율'] for p in products) / 10

    return {
        'brand': brand,
        'total_sales': total_sales,
        'best10_sales': best10_total,
        'best10_ratio': best10_total / total_sales * 100 if total_sales > 0 else 0,
        'channels': {
            'offline': {'amount': offline, 'ratio': offline/best10_total*100 if best10_total > 0 else 0},
            'online': {'amount': online, 'ratio': online/best10_total*100 if best10_total > 0 else 0},
            'dutyfree': {'amount': dutyfree, 'ratio': dutyfree/best10_total*100 if best10_total > 0 else 0}
        },
        'avg_tag': avg_tag,
        'avg_discount': avg_discount,
        'avg_actual_price': avg_tag * (1 - avg_discount),
        'products': products,
        'categories': categories,
        'growth_count': len(growth),
        'decline_count': len(decline),
        'top_growth': max(products, key=lambda x: x['전주대비']),
        'top_decline': min(products, key=lambda x: x['전주대비']),
        'growth_items': sorted(growth, key=lambda x: x['전주대비'], reverse=True),
        'decline_items': sorted(decline, key=lambda x: x['전주대비'])
    }

def classify_category(product_name: str) -> str:
    if not product_name:
        return '기타'
    for category, keywords in CATEGORIES.items():
        if any(kw in product_name for kw in keywords):
            return category
    return '기타'

def determine_position(share: float) -> str:
    if share >= 40:
        return "시장 리더"
    elif share >= 25:
        return "강력한 2위"
    else:
        return "도전자"

def determine_channel_type(offline: float, online: float, dutyfree: float) -> str:
    if offline >= 70:
        return "오프라인 의존"
    elif online >= 30:
        return "온라인 강세"
    elif abs(offline - dutyfree) < 20:
        return "균형형"
    else:
        return "오프라인 중심"

def determine_brand_power(avg_discount: float) -> str:
    if avg_discount < 0.30:
        return "강함 (가격 유지력)"
    elif avg_discount > 0.40:
        return "약함 (할인 의존)"
    else:
        return "보통"

def generate_recommendations(analysis: dict, brand: str) -> list:
    """포커스 브랜드 권고안 생성"""
    recs = []

    online_ratio = analysis['channels']['online']['ratio']
    if online_ratio < 15:
        recs.append({
            'priority': '🔴 긴급',
            'action': '온라인 전용 상품 기획',
            'target': f'{online_ratio:.1f}% → 20%',
            'effect': '온라인 채널 비중 확대'
        })

    if analysis['decline_count'] > analysis['growth_count']:
        recs.append({
            'priority': '🟠 단기',
            'action': '26SS 시즌 상품 조기 노출',
            'target': '다운 의존도 탈피',
            'effect': '시즌 전환 대응'
        })

    top_growth = analysis['top_growth']
    if top_growth['전주대비'] > 0.5:
        recs.append({
            'priority': '🟡 중기',
            'action': f"{top_growth['품명']} 파생상품 개발",
            'target': '성장 카테고리 확대',
            'effect': '히트 상품 라인업 강화'
        })

    # IP 관련 상품 체크
    ip_items = [p for p in analysis['products'] if '키키' in p['품명'] or '로고' in p['품명']]
    if len(ip_items) >= 3:
        recs.append({
            'priority': '🟢 지속',
            'action': 'IP/로고 상품 라인업 강화',
            'target': 'IP 인지도 → 충성도 전환',
            'effect': '브랜드 차별화 지속'
        })

    return recs

def generate_comparison_report(analyses: dict, focus_brand: str) -> str:
    """비교 분석 보고서 생성"""
    report = []

    # 총 매출 계산
    total_market = sum(a['total_sales'] for a in analyses.values())

    # 점유율 계산
    for brand, analysis in analyses.items():
        analysis['share'] = analysis['total_sales'] / total_market * 100 if total_market > 0 else 0
        analysis['position'] = determine_position(analysis['share'])
        analysis['channel_type'] = determine_channel_type(
            analysis['channels']['offline']['ratio'],
            analysis['channels']['online']['ratio'],
            analysis['channels']['dutyfree']['ratio']
        )
        analysis['brand_power'] = determine_brand_power(analysis['avg_discount'])

    # 보고서 생성
    report.append("# 주간 브랜드 비교 분석 보고서")
    report.append(f"**기간**: 2026년 1월 26일(월) ~ 2월 1일(일) | 1월 5주차")
    report.append(f"**분석일**: {datetime.now().strftime('%Y-%m-%d')}")
    report.append(f"**포커스 브랜드**: {focus_brand}")
    report.append("")
    report.append("---")
    report.append("")

    # Executive Summary
    report.append("## Executive Summary")
    report.append("")

    # 핵심 메시지
    focus = analyses[focus_brand]
    leader = max(analyses.values(), key=lambda x: x['share'])
    report.append(f"> **핵심 메시지**: {leader['brand']}의 시장 지배력 유지 속에서 각 브랜드별 차별화 전략 필요. ")
    report.append(f"> {focus_brand}는 {focus['channel_type']} 채널 구조로 온라인 강화 시급.")
    report.append("")

    # 요약 테이블
    report.append("| 브랜드 | 기간 매출 | 점유율 | 평균 할인율 | 브랜드 파워 | 채널 유형 |")
    report.append("|--------|----------|--------|------------|------------|----------|")
    for brand in ['커버낫', '리(LEE)', '와키윌리']:
        a = analyses[brand]
        marker = "**" if brand == focus_brand else ""
        report.append(f"| {marker}{brand}{marker} | {a['total_sales']/100000000:.1f}억원 | {a['share']:.1f}% | {a['avg_discount']*100:.1f}% | {a['brand_power']} | {a['channel_type']} |")
    report.append("")
    report.append("---")
    report.append("")

    # 브랜드별 상세 분석
    report.append("## 1. 브랜드별 상세 분석")
    report.append("")

    for brand in ['커버낫', '리(LEE)', '와키윌리']:
        a = analyses[brand]
        report.append(f"### 1.{list(analyses.keys()).index(brand)+1} {brand}")
        report.append("")
        report.append("#### 개요")
        report.append(f"| 지표 | 값 | 비고 |")
        report.append("|------|----|----|")
        report.append(f"| 기간 매출 | {a['total_sales']/100000000:.1f}억원 | {a['position']} |")
        report.append(f"| BEST 10 매출 | {a['best10_sales']/100000000:.2f}억원 | 전체의 {a['best10_ratio']:.1f}% |")
        report.append(f"| 평균 할인율 | {a['avg_discount']*100:.1f}% | {a['brand_power']} |")
        report.append("")

        report.append("#### 채널 믹스")
        report.append("```")
        offline_bar = "█" * int(a['channels']['offline']['ratio'] / 2)
        online_bar = "█" * int(a['channels']['online']['ratio'] / 2)
        dutyfree_bar = "█" * int(a['channels']['dutyfree']['ratio'] / 2)
        report.append(f"오프라인: {offline_bar} {a['channels']['offline']['ratio']:.1f}%")
        report.append(f"온라인:   {online_bar} {a['channels']['online']['ratio']:.1f}%")
        report.append(f"면세:     {dutyfree_bar} {a['channels']['dutyfree']['ratio']:.1f}%")
        report.append("```")
        report.append("")

        report.append("#### BEST 10 상품")
        report.append("| 순위 | 품명 | TAG가 | 판매수량 | 판매금액 | 전주대비 |")
        report.append("|------|------|-------|---------|----------|----------|")
        for p in a['products']:
            wow = p['전주대비']
            wow_str = f"+{wow*100:.1f}%" if wow > 0 else f"{wow*100:.1f}%"
            badge = "**" if abs(wow) > 0.5 else ""
            report.append(f"| {p['순위']} | {p['품명']} | ₩{p['TAG가']:,.0f} | {p['판매수량']:.0f}개 | {p['판매금액']/10000:.0f}만원 | {badge}{wow_str}{badge} |")
        report.append("")

        # 강점/약점
        report.append("#### 강점/약점")
        report.append("| 강점 | 약점 |")
        report.append("|------|------|")

        strengths = []
        weaknesses = []

        if a['share'] >= 40:
            strengths.append("압도적 시장 점유율")
        if a['avg_discount'] < 0.30:
            strengths.append("낮은 할인율 (브랜드 파워)")
        if a['channels']['dutyfree']['ratio'] > 25:
            strengths.append("면세 채널 강세")
        if a['growth_count'] > a['decline_count']:
            strengths.append("성장 상품 다수")
        if a['top_growth']['전주대비'] > 1:
            strengths.append(f"급성장 상품 보유 (+{a['top_growth']['전주대비']*100:.0f}%)")

        if a['avg_discount'] > 0.35:
            weaknesses.append("높은 할인율 (마진 압박)")
        if a['channels']['online']['ratio'] < 15:
            weaknesses.append("온라인 채널 취약")
        if a['channels']['dutyfree']['ratio'] < 10:
            weaknesses.append("면세 채널 취약")
        if a['decline_count'] > a['growth_count']:
            weaknesses.append("하락 상품 다수")

        if not strengths:
            strengths.append("분석 중")
        if not weaknesses:
            weaknesses.append("분석 중")

        for s, w in zip(strengths + [''] * 5, weaknesses + [''] * 5):
            if s or w:
                report.append(f"| ✅ {s} | ⚠️ {w} |")
        report.append("")
        report.append("---")
        report.append("")

    # 비교 분석
    report.append("## 2. 브랜드 비교 분석")
    report.append("")

    report.append("### 2.1 채널 전략 비교")
    report.append("| 채널 | 커버낫 | 리(LEE) | 와키윌리 | 시사점 |")
    report.append("|------|--------|---------|----------|--------|")
    report.append(f"| 오프라인 | {analyses['커버낫']['channels']['offline']['ratio']:.1f}% | {analyses['리(LEE)']['channels']['offline']['ratio']:.1f}% | {analyses['와키윌리']['channels']['offline']['ratio']:.1f}% | 전체 오프라인 의존 |")
    report.append(f"| 온라인 | {analyses['커버낫']['channels']['online']['ratio']:.1f}% | {analyses['리(LEE)']['channels']['online']['ratio']:.1f}% | {analyses['와키윌리']['channels']['online']['ratio']:.1f}% | 와키윌리 최저 |")
    report.append(f"| 면세 | {analyses['커버낫']['channels']['dutyfree']['ratio']:.1f}% | {analyses['리(LEE)']['channels']['dutyfree']['ratio']:.1f}% | {analyses['와키윌리']['channels']['dutyfree']['ratio']:.1f}% | 리(LEE) 강세 |")
    report.append("")

    report.append("### 2.2 가격 포지셔닝")
    report.append("| 브랜드 | 평균 TAG가 | 평균 할인율 | 실구매가 | 포지셔닝 |")
    report.append("|--------|-----------|------------|---------|----------|")
    for brand in ['커버낫', '리(LEE)', '와키윌리']:
        a = analyses[brand]
        pos = "프리미엄" if a['avg_tag'] > 150000 else "미드" if a['avg_tag'] > 100000 else "엔트리"
        report.append(f"| {brand} | ₩{a['avg_tag']:,.0f} | {a['avg_discount']*100:.1f}% | ₩{a['avg_actual_price']:,.0f} | {pos} |")
    report.append("")

    # 성장/하락 트렌드
    report.append("## 3. 성장/하락 트렌드")
    report.append("")

    # 전체 성장 상품 수집
    all_growth = []
    all_decline = []
    for brand, a in analyses.items():
        for p in a['growth_items']:
            all_growth.append({'brand': brand, **p})
        for p in a['decline_items']:
            all_decline.append({'brand': brand, **p})

    all_growth.sort(key=lambda x: x['전주대비'], reverse=True)
    all_decline.sort(key=lambda x: x['전주대비'])

    report.append("### 급성장 상품 TOP 5")
    report.append("| 순위 | 브랜드 | 상품 | 성장률 |")
    report.append("|------|--------|------|--------|")
    for i, p in enumerate(all_growth[:5], 1):
        report.append(f"| {i} | {p['brand']} | {p['품명']} | **+{p['전주대비']*100:.1f}%** |")
    report.append("")

    report.append("### 급하락 상품 TOP 5")
    report.append("| 순위 | 브랜드 | 상품 | 하락률 |")
    report.append("|------|--------|------|--------|")
    for i, p in enumerate(all_decline[:5], 1):
        report.append(f"| {i} | {p['brand']} | {p['품명']} | {p['전주대비']*100:.1f}% |")
    report.append("")

    # 인사이트
    report.append("## 4. 전략적 인사이트")
    report.append("")

    report.append("### 4.1 공통 트렌드")
    report.append("1. **시즌 전환기 진입**: 다운/패딩류 전반 하락, 경량 상의 상승")
    report.append("2. **로고 플레이 지속**: 세 브랜드 모두 로고 상품 상위권")
    report.append("3. **오프라인 채널 의존**: D2C 온라인 강화 필요성 공통")
    report.append("")

    report.append(f"### 4.2 {focus_brand} 실행 권고안")
    recs = generate_recommendations(analyses[focus_brand], focus_brand)
    report.append("| 우선순위 | 액션 | 목표 | 기대 효과 |")
    report.append("|----------|------|------|----------|")
    for r in recs:
        report.append(f"| {r['priority']} | {r['action']} | {r['target']} | {r['effect']} |")
    report.append("")

    # 결론
    report.append("## 5. 결론")
    report.append("")
    report.append("### 시장 현황 요약")
    report.append("```")
    report.append(f"  커버낫: 볼륨 리더 (점유율 {analyses['커버낫']['share']:.1f}%, 할인 의존 성장)")
    report.append(f"  리(LEE): 가치 리더 (할인율 {analyses['리(LEE)']['avg_discount']*100:.1f}%, 면세 강세)")
    report.append(f"  와키윌리: IP 차별화 (성장 잠재력, 채널 다변화 시급)")
    report.append("```")
    report.append("")

    report.append(f"### {focus_brand} 핵심 메시지")
    report.append("")
    report.append(f"> **\"IP로 차별화하되, 채널로 성장하라\"**")
    report.append(">")
    report.append(f"> 온라인 채널 비중 {analyses[focus_brand]['channels']['online']['ratio']:.1f}%는 업계 최저 수준.")
    report.append("> 단기적으로 온라인 전용 상품과 D2C 투자가 성장의 열쇠.")
    report.append("")
    report.append("---")
    report.append(f"*이 보고서는 AI Brand Comparison Analyzer에 의해 자동 생성되었습니다.*")

    return "\n".join(report)

def main():
    if len(sys.argv) < 2:
        print("Usage: python compare_brands.py <file_path> [focus_brand]")
        sys.exit(1)

    file_path = sys.argv[1]
    focus_brand = sys.argv[2] if len(sys.argv) > 2 else '와키윌리'

    print(f"Loading data from: {file_path}")
    df = load_data(file_path)

    # Phase 1: 개별 브랜드 분석
    print("\n[Phase 1] 개별 브랜드 분석")
    analyses = {}
    for brand in ['커버낫', '와키윌리', '리(LEE)']:
        print(f"  Analyzing {brand}...")
        analyses[brand] = analyze_single_brand(df, brand)

    # Phase 2: 비교 분석
    print("\n[Phase 2] 비교 분석 및 보고서 생성")
    report = generate_comparison_report(analyses, focus_brand)

    # 보고서 출력
    print("\n" + "=" * 80 + "\n")
    print(report)

    # 파일 저장
    output_dir = Path(file_path).parent.parent / "01_Strategy" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"weekly_brand_comparison_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n보고서 저장됨: {output_file}")

    # JSON 데이터 저장
    for brand, analysis in analyses.items():
        json_file = output_dir / f"brand_analysis_{brand}_{datetime.now().strftime('%Y%m%d')}.json"
        # products 내 non-serializable 제거
        analysis_clean = {k: v for k, v in analysis.items() if k != 'products'}
        analysis_clean['products'] = [
            {k: v for k, v in p.items() if isinstance(v, (int, float, str, bool, type(None)))}
            for p in analysis['products']
        ]
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_clean, f, ensure_ascii=False, indent=2)
    print(f"분석 데이터 저장됨: {output_dir}/brand_analysis_*.json")

if __name__ == "__main__":
    main()
