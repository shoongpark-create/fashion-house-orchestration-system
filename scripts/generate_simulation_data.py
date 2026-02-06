import csv
import random

# 파일 경로 정의
wbr_path = "/Users/sherman/Library/Mobile Documents/iCloud~md~obsidian/Documents/Sherman/00. Inbox/09. Opencode/output/wbr_data_template.csv"
mbr_path = "/Users/sherman/Library/Mobile Documents/iCloud~md~obsidian/Documents/Sherman/00. Inbox/09. Opencode/output/mbr_data_template.csv"

# ---------------------------------------------------------
# 1. 카테고리 및 상품 구조 정의 (요청사항 반영)
# ---------------------------------------------------------
categories = {
    "Apparel": [
        "Uni Outer",
        "Uni Inner",
        "Uni Bottom",
        "Womens Outer",
        "Womens Inner",
        "Womens Bottom",
    ],
    "Accessories": ["Ball Cap", "Backpack", "Scarf"],  # 아이템별
    "Shoes": ["Sneakers", "Boots", "Slides"],  # 아이템별
}

# 상품 목록 (가상 생성)
products = [
    # Apparel - Uni
    {
        "name": "Heavy Duck Down Parka",
        "cat": "Uni Outer",
        "price": 250000,
        "trend": "down",
    },
    {
        "name": "Reversible Fleece Jacket",
        "cat": "Uni Outer",
        "price": 120000,
        "trend": "flat",
    },
    {
        "name": "Oversized Logo Hoodie",
        "cat": "Uni Inner",
        "price": 79000,
        "trend": "up",
    },
    {"name": "Basic Sweatshirt Set", "cat": "Uni Inner", "price": 89000, "trend": "up"},
    {"name": "Wide Cargo Pants", "cat": "Uni Bottom", "price": 69000, "trend": "up"},
    # Apparel - Womens
    {
        "name": "Wool Balmacaan Coat",
        "cat": "Womens Outer",
        "price": 290000,
        "trend": "down",
    },
    {
        "name": "Crop Tweed Jacket",
        "cat": "Womens Outer",
        "price": 150000,
        "trend": "up",
    },
    {
        "name": "Cashmere Blend Knit",
        "cat": "Womens Inner",
        "price": 110000,
        "trend": "flat",
    },
    {
        "name": "Slim Fit Turtleneck",
        "cat": "Womens Inner",
        "price": 45000,
        "trend": "flat",
    },
    {
        "name": "Pleated Mini Skirt",
        "cat": "Womens Bottom",
        "price": 59000,
        "trend": "up",
    },
    # Accessories
    {
        "name": "Signature Ball Cap (Navy)",
        "cat": "Ball Cap",
        "price": 39000,
        "trend": "flat",
    },
    {
        "name": "Tech Backpack (Black)",
        "cat": "Backpack",
        "price": 129000,
        "trend": "explode",
    },  # 신학기
    {"name": "Soft Muffler", "cat": "Scarf", "price": 29000, "trend": "down"},
    # Shoes
    {
        "name": "Retro Runner Sneakers",
        "cat": "Sneakers",
        "price": 109000,
        "trend": "explode",
    },
    {"name": "Chunky Chelsea Boots", "cat": "Boots", "price": 149000, "trend": "down"},
    {"name": "Logo Slide", "cat": "Slides", "price": 39000, "trend": "flat"},
]


# ---------------------------------------------------------
# 2. WBR 데이터 생성 함수
# ---------------------------------------------------------
def generate_wbr():
    lines = []

    # [SECTION 1: WEEKLY_KPI]
    lines.append("# [SECTION 1: WEEKLY_KPI]")
    lines.append(
        "total_revenue,revenue_target,revenue_achievement_rate,wow_growth_rate,inventory_risk_count"
    )
    # 시나리오: 목표 대비 92% 달성, 전주 대비 5% 성장, 재고 리스크 4건
    lines.append("185000000,200000000,92.5,5.2,4")
    lines.append("")

    # [SECTION 2: CHANNEL_PERFORMANCE]
    lines.append("# [SECTION 2: CHANNEL_PERFORMANCE]")
    lines.append(
        "channel_name,channel_category,revenue,target_achievement_rate,wow_growth_rate,discount_rate,status_code,issue_note"
    )
    lines.append("Official Store,Online,85000000,95,8,10,GREEN,None")
    lines.append("Musinsa,Online,65000000,88,2,15,YELLOW,Traffic Slowdown")
    lines.append("Dept Store (Offline),Offline,35000000,92,4,5,GREEN,None")
    lines.append("")

    # [SECTION 3: CATEGORY_MATRIX]
    lines.append("# [SECTION 3: CATEGORY_MATRIX]")
    lines.append(
        "category_name,sales_qty,discount_rate,revenue_impact_score,status_label"
    )
    # 카테고리별 요약 데이터
    lines.append("Uni Outer,500,30,85,Cash Cow (Fading)")
    lines.append("Uni Inner,1200,5,70,Rising Star")
    lines.append("Sneakers,800,0,90,Hero Item")
    lines.append("Womens Bottom,300,5,40,Question Mark")
    lines.append("")

    # [SECTION 4: ACTION_ALERTS]
    lines.append("# [SECTION 4: ACTION_ALERTS]")
    lines.append(
        "alert_type,item_name,urgency_level,metric_value,metric_unit,recommended_action"
    )
    lines.append("Restock,Retro Runner Sneakers,URGENT,0.8,weeks,Emergency Order")
    lines.append("Promo,Heavy Duck Down Parka,NORMAL,45,%,End of Season Sale")
    lines.append("")

    # [SECTION 5: WEEKLY_BEST_10]
    lines.append("# [SECTION 5: WEEKLY_BEST_10]")
    lines.append("rank,product_name,qty,wow_percent")
    # 수량 기준 정렬 (가상 로직)
    sorted_by_qty = sorted(
        products,
        key=lambda x: 100
        if x["trend"] == "down"
        else (500 if x["trend"] == "up" else 1000),
        reverse=True,
    )
    # 수동 설정으로 스토리 부여
    best_10 = [
        ("Retro Runner Sneakers", 1250, 45),
        ("Oversized Logo Hoodie", 980, 15),
        ("Basic Sweatshirt Set", 850, 10),
        ("Tech Backpack (Black)", 600, 120),  # 폭발적 성장
        ("Wide Cargo Pants", 550, 8),
        ("Signature Ball Cap (Navy)", 400, 2),
        ("Heavy Duck Down Parka", 350, -15),
        ("Reversible Fleece Jacket", 300, -5),
        ("Pleated Mini Skirt", 280, 12),
        ("Logo Slide", 200, 0),
    ]
    for idx, item in enumerate(best_10):
        lines.append(f"{idx + 1},{item[0]},{item[1]},{item[2]}")
    lines.append("")

    # [SECTION 6: WEEKLY_TREND] - 4주치 데이터
    lines.append("# [SECTION 6: WEEKLY_TREND]")
    lines.append("week_label,category_name,revenue")
    weeks = ["W-01", "W-02", "W-03", "W-04"]

    # 카테고리별 트렌드 시뮬레이션
    simulated_categories = {
        "Uni Outer": [5000, 4500, 4000, 3500],  # 하락
        "Uni Inner": [2000, 2500, 3000, 3800],  # 상승
        "Womens Outer": [3000, 2800, 2500, 2000],  # 하락
        "Sneakers": [1000, 1500, 3000, 5500],  # 급상승
        "Backpack": [800, 1000, 1500, 2500],  # 신학기 상승
        "Womens Inner": [1500, 1600, 1700, 1800],  # 완만 상승
    }

    for wk_idx, week in enumerate(weeks):
        for cat, rev_list in simulated_categories.items():
            # 단위: 만원 -> 원
            lines.append(f"{week},{cat},{rev_list[wk_idx] * 10000}")
    lines.append("")

    # [SECTION 7: WEEKLY_VOC_STATS]
    lines.append("# [SECTION 7: WEEKLY_VOC_STATS]")
    lines.append("total_reviews,cs_response_rate,sentiment_score")
    lines.append("2100,95,78")  # 긍정 비율 78% (스니커즈 인기 vs 배송 지연)
    lines.append("")

    # [SECTION 8: WEEKLY_VOC_KEYWORDS]
    lines.append("# [SECTION 8: WEEKLY_VOC_KEYWORDS]")
    lines.append("keyword,type,count")
    lines.append("실물깡패,Positive,320")
    lines.append("착화감,Positive,210")
    lines.append("핏예술,Positive,150")
    lines.append("배송지연,Negative,120")  # 주문 폭주로 인한 지연
    lines.append("사이즈큼,Negative,80")
    lines.append("보풀,Negative,40")
    lines.append("")

    # [SECTION 9: WEEKLY_HOT_TOPIC]
    lines.append("# [SECTION 9: WEEKLY_HOT_TOPIC]")
    lines.append("product_name,category,voc_growth_rate,feedback_1,feedback_2")
    lines.append(
        "Retro Runner Sneakers,Shoes,+300%,Best shoes ever consistent size,Delivery took 5 days"
    )
    lines.append("")

    # [SECTION 10: WEEKLY_PARETO]
    lines.append("# [SECTION 10: WEEKLY_PARETO]")
    lines.append("category_name,top_20_share,status")
    lines.append("Uni Outer,85,Concentrated")
    lines.append("Uni Inner,50,Good")
    lines.append("Shoes,90,Risk (Single Hero)")  # 스니커즈 하나에 너무 의존
    lines.append("Womens Bottom,35,Fragmented")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------
# 3. MBR 데이터 생성 함수
# ---------------------------------------------------------
def generate_mbr():
    lines = []

    # [SECTION 1: MONTHLY_HEALTH]
    lines.append("# [SECTION 1: MONTHLY_HEALTH]")
    lines.append("op_margin,return_rate,roas")
    lines.append("18.5,4.2,420")  # 이익률 양호, 반품률 낮음, ROAS 우수
    lines.append("")

    # [SECTION 2: CHANNEL_PROFIT]
    lines.append("# [SECTION 2: CHANNEL_PROFIT]")
    lines.append(
        "channel_name,channel_category,revenue,contribution_margin,marketing_spend"
    )
    lines.append("Official Store,Online,350000000,45,50000000")
    lines.append("Musinsa,Online,280000000,20,80000000")
    lines.append("Dept Store,Offline,150000000,35,20000000")
    lines.append("")

    # [SECTION 3: PRODUCT_QUALITY]
    lines.append("# [SECTION 3: PRODUCT_QUALITY]")
    lines.append("product_name,net_sales_qty,return_rate,quality_status")
    lines.append("Retro Runner Sneakers,3500,2.5,Hidden Gem")  # 많이 팔리는데 반품 적음
    lines.append("Pleated Mini Skirt,800,18.5,Toxic Hero")  # 핏 문제로 반품 높음
    lines.append("Heavy Duck Down Parka,1200,5.0,Cash Cow")
    lines.append("Tech Backpack,900,1.2,Star")
    lines.append("")

    # [SECTION 4: STRATEGIC_DECISIONS]
    lines.append("# [SECTION 4: STRATEGIC_DECISIONS]")
    lines.append("decision_type,item_name,reason,action_plan")
    lines.append(
        "EXPAND,Retro Runner Sneakers,Explosive Viral Growth,Add 2 New Colorways"
    )
    lines.append(
        "REVAMP,Pleated Mini Skirt,High Return Rate (Fit Issue),Adjust Waist Pattern"
    )
    lines.append("DROP,Chunky Chelsea Boots,Trend Decline,Final Clearance")
    lines.append("")

    # [SECTION 5: MONTHLY_BEST_10]
    lines.append("# [SECTION 5: MONTHLY_BEST_10]")
    lines.append("rank,product_name,revenue,margin_percent")
    lines.append("1,Heavy Duck Down Parka,300000000,25")
    lines.append("2,Retro Runner Sneakers,150000000,45")  # 마진 좋음
    lines.append("3,Oversized Logo Hoodie,90000000,35")
    lines.append("4,Wool Balmacaan Coat,85000000,20")
    lines.append("5,Tech Backpack (Black),70000000,50")  # 가방 마진 높음
    lines.append("6,Basic Sweatshirt Set,65000000,30")
    lines.append("7,Reversible Fleece,60000000,22")
    lines.append("8,Wide Cargo Pants,55000000,33")
    lines.append("9,Crop Tweed Jacket,40000000,40")
    lines.append("10,Signature Ball Cap,35000000,55")
    lines.append("")

    # [SECTION 6: MONTHLY_PARETO]
    lines.append("# [SECTION 6: MONTHLY_PARETO]")
    lines.append("category_name,top_20_share,status")
    lines.append("Uni Outer,82,Concentrated")  # 겨울 끝자락이라 소수 인기제품만 팔림
    lines.append("Shoes,88,Risk")  # 스니커즈 독주
    lines.append("Accessories,40,Good")
    lines.append("Uni Inner,55,Good")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------
# 파일 쓰기
# ---------------------------------------------------------
wbr_content = generate_wbr()
with open(wbr_path, "w", encoding="utf-8") as f:
    f.write(wbr_content)

mbr_content = generate_mbr()
with open(mbr_path, "w", encoding="utf-8") as f:
    f.write(mbr_content)

print("Data generation complete.")
