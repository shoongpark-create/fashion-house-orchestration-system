import os
import sys

# Output directory setup
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class BusinessReviewDashboard:
    def __init__(self):
        self.data = {
            "summary": {
                "total_revenue": 54.04,  # 억 원
                "target": 71.70,
                "achievement_rate": 75,
                "yoy_growth": -21.4,
                "cost_rate": 37,
                "cost_rate_diff": -8,  # %p
                "profit_rate": 63,
                "profit_rate_diff": +8,  # %p
                "discount_rate": 35,
                "discount_rate_diff": -6.1,
            },
            "channels": [
                {
                    "name": "Online Total",
                    "revenue": 9.23,
                    "yoy": -33.0,
                    "achievement": 70,
                    "share": 17,
                },
                {
                    "name": "- Own Mall",
                    "revenue": 4.18,
                    "yoy": 33.5,
                    "achievement": 70,
                    "share": 8,
                },
                {
                    "name": "- Musinsa",
                    "revenue": 4.65,
                    "yoy": -35.3,
                    "achievement": 72,
                    "share": 9,
                },
                {
                    "name": "Offline (Shop-in-shop)",
                    "revenue": 28.85,
                    "yoy": -19.9,
                    "achievement": 70,
                    "share": 53,
                },
                {
                    "name": "Retail (FSS/DutyFree)",
                    "revenue": 15.61,
                    "yoy": -17.4,
                    "achievement": 98,
                    "share": 29,
                },
            ],
            "categories": [
                {
                    "name": "Down Parka",
                    "revenue": 11.69,
                    "yoy": -43,
                    "discount": 35,
                    "status": "WORST",
                },
                {
                    "name": "Jacket",
                    "revenue": 4.67,
                    "yoy": +13,
                    "discount": 29,
                    "status": "BEST",
                },
                {
                    "name": "Knit",
                    "revenue": 1.80,
                    "yoy": +22,
                    "discount": 28,
                    "status": "BEST",
                },
                {
                    "name": "Bag",
                    "revenue": 0.93,
                    "yoy": -28,
                    "discount": 15,
                    "status": "BAD",
                },  # 12월 기준
                {
                    "name": "Muffler",
                    "revenue": 0.60,
                    "yoy": -61,
                    "discount": 20,
                    "status": "WORST",
                },
            ],
            "issues": [
                "**[Down Parka]** Weather impact (late winter) & lack of differentiation -> -43% YoY.",
                "**[Musinsa]** Black Friday timing mismatch & platform traffic decline -> -35% YoY.",
                "**[Online]** High discount dependency, lack of hero items for normal price conversion.",
                "**[Retail]** Duty Free performed well (101% achievement) with lower discount rate (29%).",
            ],
            "action_items": [
                "**[Jan Strategy]** Focus on 26SS Bags for Back-to-School season (New Hero Item).",
                "**[Profitability]** Shift Online CPS to focus on ROAS/Profit rather than volume.",
                "**[Inventory]** 25FW Down Parka carry-over plan & early season-off for winter stock.",
                "**[Woman]** Focus on expanding Woman's line (Knit/Coat sales good).",
            ],
        }

    def generate_dashboard(self):
        d = self.data
        s = d["summary"]

        # Dashboard Header
        md = f"# 📊 Wacky Willy December Business Review Dashboard\n\n"

        # 1. Executive Summary (KPI Cards)
        md += "## 1. Executive Summary (KPIs)\n"
        md += "| Metric | Value | Target | YoY | Status |\n"
        md += "|---|---|---|---|---|\n"

        # Status Logic
        rev_status = "🔴" if s["achievement_rate"] < 80 else "🟢"
        yoy_status = "🔻" if s["yoy_growth"] < 0 else "🔺"

        md += f"| **Revenue** | **{s['total_revenue']}억** | {s['target']}억 (75%) | {s['yoy_growth']}% | {rev_status} {yoy_status} |\n"
        md += f"| **Gross Margin** | {s['profit_rate']}% | - | +{s['profit_rate_diff']}%p | 🟢 Profit Improved |\n"
        md += f"| **Discount Rate** | {s['discount_rate']}% | - | {s['discount_rate_diff']}%p | 🟢 Discount Controlled |\n"
        md += "\n"

        # 2. Channel Analysis
        md += "## 2. Channel Performance Analysis\n"
        md += "> **Insight**: Online & Dept Stores struggled, but Duty Free & Outlets defended the baseline.\n\n"
        md += "| Channel | Revenue (억) | Share | YoY | Achievement |\n"
        md += "|---|---|---|---|---|\n"
        for c in d["channels"]:
            icon = "🔻" if c["yoy"] < 0 else "🔺"
            md += f"| {c['name']} | {c['revenue']} | {c['share']}% | {c['yoy']}% {icon} | {c['achievement']}% |\n"
        md += "\n"

        # 3. Category Deep Dive (25FW)
        md += "## 3. Product Category Deep Dive (25FW)\n"
        md += "### 🏆 Winners & 📉 Losers\n"

        md += "| Category | Revenue (백만) | YoY | Discount | Analysis |\n"
        md += "|---|---|---|---|---|\n"
        for cat in d["categories"]:
            status_icon = (
                "🔥"
                if cat["status"] == "BEST"
                else ("⚠️" if cat["status"] == "BAD" else "🚨")
            )
            # Revenue value in the object is in 억 for dashboard simplicity, but let's format nicely
            md += f"| {cat['name']} | {int(cat['revenue'] * 100)}M | {cat['yoy']}% | {cat['discount']}% | {status_icon} {cat['status']} |\n"

        md += "\n"

        # 4. Critical Issues & Action Plan
        md += "## 4. Key Issues & Action Plan (Jan)\n"

        md += "### 🚨 Critical Issues\n"
        for issue in d["issues"]:
            md += f"- {issue}\n"

        md += "\n### 🚀 Action Plan (Jan)\n"
        for action in d["action_items"]:
            md += f"- {action}\n"

        # Write to file
        output_path = f"{OUTPUT_DIR}/December_Business_Dashboard.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md)

        print(f"✅ Dashboard generated: {output_path}")


if __name__ == "__main__":
    dashboard = BusinessReviewDashboard()
    dashboard.generate_dashboard()
