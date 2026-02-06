import pandas as pd
import os


class DataEngine:
    def __init__(self, macro_file, micro_file):
        self.macro_file = macro_file
        self.micro_file = micro_file

    def load_macro_data(self):
        """Loads channel/season summary data."""
        try:
            df = pd.read_excel(
                self.macro_file, sheet_name=0, engine="openpyxl", header=None
            )
            summary_data = []
            current_channel = "Unknown"

            for index, row in df.iterrows():
                if index < 4:
                    continue

                if pd.notna(row[2]):
                    current_channel = row[2]

                season = row[4]
                if (
                    pd.notna(season)
                    and isinstance(season, str)
                    and season in ["26SS", "25FW", "25SS", "24FW", "이월"]
                ):
                    sales = pd.to_numeric(row[5], errors="coerce") or 0
                    growth = pd.to_numeric(row[9], errors="coerce") or 0

                    summary_data.append(
                        {
                            "Channel": current_channel,
                            "Season": season,
                            "Sales": sales,
                            "Growth Rate": growth,
                        }
                    )

            return pd.DataFrame(summary_data)
        except Exception as e:
            print(f"Error loading macro data: {e}")
            return pd.DataFrame()

    def load_micro_data(self):
        """Loads Best 10 SKU data."""
        try:
            df = pd.read_excel(
                self.micro_file, engine="openpyxl", header=None, skiprows=3
            )
            best_items = []

            sku_row = 5
            name_row = 6
            price_row = 7
            qty_row = 8
            sales_amt_row = 10

            for col in range(len(df.columns)):
                val = df.iloc[sku_row, col]
                if (
                    pd.notna(val)
                    and isinstance(val, str)
                    and len(val) > 5
                    and val != "품번"
                ):
                    item = {
                        "SKU": val,
                        "Product Name": df.iloc[name_row, col],
                        "Price": pd.to_numeric(df.iloc[price_row, col], errors="coerce")
                        or 0,
                        "Qty": pd.to_numeric(df.iloc[qty_row, col], errors="coerce")
                        or 0,
                        "Sales Amount": pd.to_numeric(
                            df.iloc[sales_amt_row, col], errors="coerce"
                        )
                        or 0,
                    }
                    best_items.append(item)

            return pd.DataFrame(best_items).sort_values(
                by="Sales Amount", ascending=False
            )
        except Exception as e:
            print(f"Error loading micro data: {e}")
            return pd.DataFrame()
