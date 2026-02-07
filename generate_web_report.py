import pandas as pd
import numpy as np
import os
import json
from datetime import datetime

FILE_PATH = "Sherman's Workspace/Data/Wacky_Sales_Data_Cleaned.xlsx"
OUTPUT_DIR = "Sherman's Workspace/output"
TEMPLATE_PATH = "Sherman's Workspace/output/dashboard_template.html"
CURRENT_YEAR = 26
REF_YEAR = 25


class WackyDashboardGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ss26 = None
        self.ss25 = None
        self.report_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def _clean_header(self, df):
        new_columns = []
        for col in df.columns:
            top = (
                str(col[0]).strip()
                if not pd.isna(col[0]) and "Unnamed" not in str(col[0])
                else ""
            )
            sub = (
                str(col[1]).strip()
                if not pd.isna(col[1]) and "Unnamed" not in str(col[1])
                else ""
            )

            if top and sub:
                new_col = top if top == sub else f"{top}_{sub}"
            elif top:
                new_col = top
            elif sub:
                new_col = sub
            else:
                new_col = f"Column_{len(new_columns)}"
            new_columns.append(new_col)
        df.columns = new_columns
        return df

    def _process_data(self, df, target_year=None):
        if isinstance(df.columns, pd.MultiIndex):
            df = self._clean_header(df)

        if "기획정보_시즌" in df.columns:
            df = df[df["기획정보_시즌"].isin(["봄", "여름"])].copy()

        if target_year:
            # Check for MultiIndex '기획정보' -> '연도' or flat '기획정보_연도'
            col_year = None
            if ("기획정보", "연도") in df.columns:
                col_year = ("기획정보", "연도")
            elif "기획정보_연도" in df.columns:
                col_year = "기획정보_연도"

            if col_year:
                # Convert to numeric, handle NaN, then cast to int for safe comparison
                # This ensures 25.0 matches 25
                df[col_year] = (
                    pd.to_numeric(df[col_year], errors="coerce").fillna(0).astype(int)
                )
                df = df[df[col_year] == int(target_year)].copy()

        cols_to_num = [
            "발주_수량",
            "발주_금액",
            "누계입고_수량",
            "누계입고_금액",
            "기간판매_수량",
            "기간판매_금액",
            "누계판매_수량",
            "누계판매_금액",
            "총재고_수량",
            "총재고_금액",
            "기간판매(TO일자 - 7)_금액",
        ]
        for col in cols_to_num:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        if "누계입고_수량" in df.columns and "누계판매_수량" in df.columns:
            df["Sell_Through"] = np.where(
                df["누계입고_수량"] > 0,
                (df["누계판매_수량"] / df["누계입고_수량"] * 100),
                0,
            ).round(1)

        if "발주_수량" in df.columns and "누계입고_수량" in df.columns:
            df["In_Rate"] = np.where(
                df["발주_수량"] > 0, (df["누계입고_수량"] / df["발주_수량"] * 100), 0
            ).round(1)

        return df

    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Data file not found: {self.file_path}")

        xls = pd.ExcelFile("Sherman's Workspace/Data/와키윌리 주간판매 데이터.xlsx")
        sheet_names = xls.sheet_names
        print(f"Sheets found: {sheet_names}")

        # Load Current Year (Usually 1st sheet or explicitly named)
        # Try finding a sheet with "금년" or default to index 0
        curr_sheet = next((s for s in sheet_names if "금년" in s), sheet_names[0])
        print(f"Loading Current Year from: {curr_sheet}")
        df_curr = pd.read_excel(xls, sheet_name=curr_sheet, header=[0, 1])
        self.ss26 = self._process_data(df_curr, CURRENT_YEAR)
        self.ss26["구분"] = "금년"

        # Load Previous Year (Usually 2nd sheet or explicitly named)
        # Try finding a sheet with "전년"
        prev_sheet = next((s for s in sheet_names if "전년" in s), None)

        if prev_sheet:
            print(f"Loading Previous Year from: {prev_sheet}")
            df_prev = pd.read_excel(xls, sheet_name=prev_sheet, header=[0, 1])
            # Strictly filter for REF_YEAR (25) to avoid including Year 24 (Two Years Ago)
            self.ss25 = self._process_data(df_prev, target_year=REF_YEAR)
            self.ss25["구분"] = "전년"
        elif len(sheet_names) > 1:
            # Fallback to 2nd sheet if not named explicitly
            print(f"Loading Previous Year from index 1: {sheet_names[1]}")
            df_prev = pd.read_excel(xls, sheet_name=1, header=[0, 1])
            self.ss25 = self._process_data(df_prev, target_year=REF_YEAR)
            self.ss25["구분"] = "전년"
        else:
            print("No Previous Year sheet found.")
            self.ss25 = pd.DataFrame()

    def generate_html(self):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        if self.ss26 is None:
            raise ValueError("Data not loaded")

        # Merge Data for JS
        combined_df = self.ss26.copy()
        if self.ss25 is not None and not self.ss25.empty:
            combined_df = pd.concat([combined_df, self.ss25], ignore_index=True)

        # Columns to export to JS
        js_cols = [
            "기획정보_연도",
            "기획정보_시즌",
            "기획정보_성별",
            "기획정보_의류/용품",
            "기획정보_대복종",
            "기획정보_복종",
            "시스템정보_품번",
            "시스템정보_색상",
            "발주_수량",
            "발주_금액",
            "누계입고_수량",
            "누계입고_금액",
            "In_Rate",
            "기간판매_수량",
            "기간판매_금액",
            "누계판매_수량",
            "누계판매_금액",
            "총재고_수량",
            "총재고_금액",
            "Sell_Through",
            "구분",  # Important for Logic
        ]

        # Ensure all cols exist
        for col in js_cols:
            if col not in combined_df.columns:
                combined_df[col] = None

        item_data_json = combined_df[js_cols].to_json(orient="records")

        # Read Template
        if not os.path.exists(TEMPLATE_PATH):
            raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")

        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            html_template = f.read()

        # Replace Placeholders
        html_content = html_template.replace("{item_data_json}", item_data_json)
        html_content = html_content.replace("{report_date}", self.report_date)

        # Force cache bust with new filename pattern
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"dashboard_26ss_{timestamp}.html"
        full_path = os.path.join(OUTPUT_DIR, file_name)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ Dashboard generated: {full_path}")
        return full_path


if __name__ == "__main__":
    try:
        generator = WackyDashboardGenerator(FILE_PATH)
        generator.load_data()
        generator.generate_html()
    except Exception as e:
        print(f"Error: {e}")
