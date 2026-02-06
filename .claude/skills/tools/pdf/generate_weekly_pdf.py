import sys
import os

# Add the current directory to sys.path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_engine import DataEngine
from visualizer import Visualizer
from pdf_composer import PDFComposer


def main():
    # 1. Define Paths
    base_dir = os.getcwd()
    macro_file = os.path.join(
        base_dir, "Data/국내영업부_브랜드별 시즌 품목 판매_1월 5주차_공유.xlsx"
    )
    micro_file = os.path.join(
        base_dir, "Data/국내영업부_브랜드별 판매 BEST 10_1월5주차_공유.xlsx"
    )
    output_pdf = os.path.join(base_dir, "output/Wacky_Willy_Weekly_Review_KR.pdf")

    # 2. Load Data
    print("🚀 Loading Data...")
    engine = DataEngine(macro_file, micro_file)
    macro_df = engine.load_macro_data()
    micro_df = engine.load_micro_data()

    if macro_df.empty or micro_df.empty:
        print("❌ Error: Failed to load data. Check file paths.")
        return

    # 3. Create Visualizations
    print("🎨 Creating Visualizations...")
    viz = Visualizer(output_dir=os.path.join(base_dir, "output/charts"))
    charts = {}

    # Generate charts and store paths
    charts["channel_perf"] = viz.create_channel_performance_chart(macro_df)
    charts["growth_rate"] = viz.create_growth_chart(macro_df)
    charts["best_items_scatter"] = viz.create_best_items_scatter(
        micro_df
    )  # Updated method name

    # 4. Generate PDF
    print("📄 Composing PDF Report...")
    composer = PDFComposer(output_path=output_pdf)
    composer.create_pdf(macro_df, micro_df, charts)

    print("✅ Mission Complete!")


if __name__ == "__main__":
    main()
