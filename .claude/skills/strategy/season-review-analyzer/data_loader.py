# scripts/review_system/dummy_data.py

# 1. Sales & Return Data (Quant + QC)
SALES_DATA = [
    {
        "sku": "FW25-PANT-004",
        "name": "Viral Wide Denim",
        "category": "Pants",
        "price": 89000,
        "initial_stock": 3000,
        "sold_qty": 2800,       # 완판 임박했으나...
        "return_qty": 840,      # 반품률 30% (심각)
        "return_reason": {"size_issue": 600, "quality_defect": 40, "simple_change": 200}
    },
    {
        "sku": "FW25-KNIT-005",
        "name": "Hidden Gem Cardigan",
        "category": "Knit",
        "price": 129000,
        "initial_stock": 500,
        "sold_qty": 150,        # 판매율 저조 (30%)
        "return_qty": 5,        # 반품률 3% (극강의 만족도)
        "return_reason": {"size_issue": 2, "quality_defect": 0, "simple_change": 3}
    },
    {
        "sku": "FW25-TOP-002",
        "name": "Basic Logo Sweat",
        "category": "Sweatshirt",
        "price": 59000,
        "initial_stock": 2000,
        "sold_qty": 900,
        "return_qty": 135,      # 반품률 15%
        "return_reason": {"quality_defect": 100, "size_issue": 10, "simple_change": 25}
    }
]

# 2. Marketing Data (Efficiency)
MARKETING_DATA = [
    {
        "sku": "FW25-PANT-004", # Viral Wide Denim
        "ad_spend": 15000000,   # 광고비 1,500만원
        "impressions": 500000,  # 노출 50만
        "clicks": 25000,        # 클릭 2.5만 (CTR 5% - 높음)
        "conversions": 1800     # 광고 기여 구매 (CVR 7.2% - 높음)
    },
    {
        "sku": "FW25-KNIT-005", # Hidden Gem Cardigan
        "ad_spend": 500000,     # 광고비 50만원 (거의 안 씀)
        "impressions": 10000,
        "clicks": 200,          # CTR 2%
        "conversions": 10       # CVR 5%
    }
]

# 3. VOC Data (Qual)
VOC_DATA = [
    {
        "sku": "FW25-PANT-004",
        "sentiment": "negative",
        "comment": "핏은 예쁜데 기장이 너무 길어요. 180cm 아니면 다 끌림. 수선비가 더 나옴."
    },
    {
        "sku": "FW25-PANT-004",
        "sentiment": "positive",
        "comment": "사진빨은 최고. 인스타 올리기 좋음."
    },
    {
        "sku": "FW25-KNIT-005",
        "sentiment": "positive",
        "comment": "이거 왜 홍보 안 하세요? 원단이 캐시미어급임. 깔별로 쟁임."
    },
    {
        "sku": "FW25-TOP-002",
        "sentiment": "negative",
        "comment": "목 늘어남 심각함."
    }
]
