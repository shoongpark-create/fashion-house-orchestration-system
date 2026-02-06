import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import os


class Visualizer:
    def __init__(self, output_dir="output/charts"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        # Set Modern Style
        sns.set_style("white")  # Remove grid background

        # Custom Font Configuration
        font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
        if os.path.exists(font_path):
            self.font_prop = fm.FontProperties(fname=font_path)
            plt.rcParams["font.family"] = self.font_prop.get_name()
        else:
            plt.rcParams["font.family"] = "sans-serif"

        plt.rcParams["axes.unicode_minus"] = False

        # Brand Colors (Wacky Willy Palette: Vivid & Street)
        self.colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEEAD"]

    def create_channel_performance_chart(self, df):
        """Bar chart for Sales by Channel & Season (Improved)."""
        if df.empty:
            return None

        plt.figure(figsize=(12, 7))

        # Data filtering
        main_seasons = ["26SS", "25FW", "25SS"]
        df_filtered = df[df["Season"].isin(main_seasons)]

        # Pivot for stacked bar (more magazine-like)
        # Actually grouped bar is better for comparison, but let's make it cleaner.

        ax = sns.barplot(
            data=df_filtered,
            x="Channel",
            y="Sales",
            hue="Season",
            palette="pastel",  # Cleaner look
            edgecolor=".2",  # Add border
            linewidth=1.5,
        )

        # Remove top/right spines
        sns.despine(trim=True)

        plt.title(
            "채널별/시즌별 주간 매출 현황",
            fontsize=20,
            pad=20,
            fontweight="bold",
            fontproperties=self.font_prop,
        )
        plt.xlabel("", fontsize=12)
        plt.ylabel("매출액 (KRW)", fontsize=12, fontproperties=self.font_prop)
        plt.legend(title="Season", frameon=False)
        plt.grid(axis="y", linestyle="--", alpha=0.3)

        # Format y-axis to readable unit (e.g. 100M)
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(
            ["{:,.0f}억".format(x / 100000000) for x in current_values],
            fontproperties=self.font_prop,
        )

        filepath = os.path.join(self.output_dir, "channel_perf.png")
        plt.savefig(filepath, dpi=300, bbox_inches="tight", transparent=True)
        plt.close()
        return filepath

    def create_growth_chart(self, df):
        """Diverging Bar chart for Growth Rate."""
        if df.empty:
            return None

        df_26ss = df[df["Season"] == "26SS"].sort_values("Growth Rate", ascending=False)

        plt.figure(figsize=(10, 6))

        # Assign colors based on positive/negative growth
        colors = ["#2ECC71" if x >= 0 else "#E74C3C" for x in df_26ss["Growth Rate"]]

        ax = sns.barplot(
            data=df_26ss, y="Channel", x="Growth Rate", palette=colors, edgecolor="none"
        )

        sns.despine(left=True, bottom=True)

        plt.title(
            "26SS 시즌 채널별 성장률 (전주 대비)",
            fontsize=20,
            pad=20,
            fontweight="bold",
            fontproperties=self.font_prop,
        )
        plt.xlabel("성장률 (%)", fontsize=12, fontproperties=self.font_prop)
        plt.ylabel("", fontsize=12)

        # Add labels directly on bars
        for i, v in enumerate(df_26ss["Growth Rate"]):
            label_x = v + 0.02 if v >= 0 else v - 0.08
            ax.text(
                label_x,
                i,
                f"{v:+.1%}",
                va="center",
                fontweight="bold",
                fontsize=12,
                color="#333333",
            )

        plt.axvline(0, color="gray", linewidth=1, linestyle="--")
        plt.grid(False)  # No grid for clean look
        plt.xticks([])  # Hide x-axis ticks

        filepath = os.path.join(self.output_dir, "growth_rate.png")
        plt.savefig(filepath, dpi=300, bbox_inches="tight", transparent=True)
        plt.close()
        return filepath

    def create_best_items_scatter(self, df):
        """Bubble chart for Price vs Volume."""
        if df.empty:
            return None

        plt.figure(figsize=(12, 8))

        # Use sales amount for bubble size
        sizes = df["Sales Amount"] / df["Sales Amount"].max() * 2000

        scatter = plt.scatter(
            x=df["Price"],
            y=df["Qty"],
            s=sizes,
            c=df["Sales Amount"],
            cmap="coolwarm",
            alpha=0.7,
            edgecolors="w",
            linewidth=2,
        )

        # Modern Style
        sns.despine()

        # Annotate top 5 items
        sorted_df = df.sort_values("Sales Amount", ascending=False).head(5)
        for i, row in sorted_df.iterrows():
            plt.text(
                row["Price"],
                row["Qty"],
                f" {row['Product Name']}",
                fontsize=10,
                fontproperties=self.font_prop,
                weight="bold",
                color="#333333",
            )

        plt.title(
            "Best 10: 가격 포지셔닝 및 판매량 분석",
            fontsize=20,
            pad=20,
            fontweight="bold",
            fontproperties=self.font_prop,
        )
        plt.xlabel("판매가 (KRW)", fontsize=12, fontproperties=self.font_prop)
        plt.ylabel("판매 수량 (Qty)", fontsize=12, fontproperties=self.font_prop)
        plt.grid(True, linestyle=":", alpha=0.4)

        # X-axis currency format
        current_values = plt.gca().get_xticks()
        plt.gca().set_xticklabels(["{:,.0f}".format(x) for x in current_values])

        filepath = os.path.join(self.output_dir, "best_items_scatter.png")
        plt.savefig(filepath, dpi=300, bbox_inches="tight", transparent=True)
        plt.close()
        return filepath
