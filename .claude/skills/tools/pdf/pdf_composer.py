from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak,
    Frame,
    PageTemplate,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect
import os
from datetime import datetime


class PDFComposer:
    def __init__(self, output_path="output/Wacky_Willy_Weekly_Review_KR.pdf"):
        self.output_path = output_path
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        # Register Korean Font
        font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
        self.font_name = "AppleGothic"
        pdfmetrics.registerFont(TTFont(self.font_name, font_path))

    def _header_footer(self, canvas, doc):
        """Draws the header and footer on each page."""
        canvas.saveState()

        # Header
        canvas.setFont(self.font_name, 10)
        canvas.setFillColor(colors.HexColor("#7f8c8d"))
        canvas.drawString(20 * mm, 285 * mm, "Wacky Willy Fashion House")
        canvas.drawRightString(
            190 * mm,
            285 * mm,
            f"Weekly Business Review | {datetime.now().strftime('%Y-%m-%d')}",
        )

        # Header Line
        canvas.setStrokeColor(colors.HexColor("#ecf0f1"))
        canvas.setLineWidth(1)
        canvas.line(20 * mm, 282 * mm, 190 * mm, 282 * mm)

        # Footer
        canvas.setFont("Helvetica", 9)
        canvas.drawCentredString(105 * mm, 15 * mm, f"Page {doc.page}")

        canvas.restoreState()

    def create_pdf(self, macro_data, micro_data, charts):
        doc = SimpleDocTemplate(
            self.output_path,
            pagesize=A4,
            rightMargin=20 * mm,
            leftMargin=20 * mm,
            topMargin=25 * mm,
            bottomMargin=25 * mm,
        )

        # Define Page Template for Header/Footer
        frame = Frame(
            doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal"
        )
        template = PageTemplate(id="report", frames=frame, onPage=self._header_footer)
        doc.addPageTemplates([template])

        styles = getSampleStyleSheet()

        # --- Custom Styles (Magazine Look) ---
        title_style = ParagraphStyle(
            "Title",
            fontName=self.font_name,
            fontSize=32,
            leading=40,
            spaceAfter=10,
            textColor=colors.HexColor("#2c3e50"),
            alignment=1,  # Center
        )

        subtitle_style = ParagraphStyle(
            "Subtitle",
            fontName=self.font_name,
            fontSize=14,
            leading=20,
            spaceAfter=30,
            textColor=colors.HexColor("#7f8c8d"),
            alignment=1,  # Center
        )

        h1_style = ParagraphStyle(
            "Heading1_KR",
            fontName=self.font_name,
            fontSize=18,
            leading=24,
            spaceBefore=20,
            spaceAfter=15,
            textColor=colors.HexColor("#e67e22"),  # Accent Color
            borderPadding=0,
        )

        body_style = ParagraphStyle(
            "Body_KR",
            fontName=self.font_name,
            fontSize=11,
            leading=18,
            spaceAfter=12,
            textColor=colors.HexColor("#34495e"),
            alignment=4,  # Justify
        )

        highlight_box = ParagraphStyle(
            "Highlight",
            parent=body_style,
            backColor=colors.HexColor("#f0f3f4"),
            borderPadding=15,
            borderRadius=5,
            spaceAfter=20,
            spaceBefore=10,
        )

        elements = []

        # ==========================================
        # 1. Cover Page
        # ==========================================
        elements.append(Spacer(1, 30 * mm))
        elements.append(
            Paragraph("Wacky Willy<br/>Weekly Business Review", title_style)
        )
        elements.append(
            Paragraph("데이터 기반 의사결정을 위한 주간 세일즈 리포트", subtitle_style)
        )

        # Key Summary Box
        summary_text = """
        <b>🚀 Executive Summary</b><br/><br/>
        이번 주, 와키윌리는 <b>26SS 신상 시즌으로의 전환</b>이 성공적으로 이루어지고 있습니다. 
        전체 매출 중 26SS 비중이 급격히 증가하며 전주 대비 <b>+46.1%</b> 성장했습니다.<br/><br/>
        
        <b>📈 핵심 포인트:</b><br/>
        • <b>자사몰 (Own Mall):</b> 이익률이 가장 높은 자사몰에서 신상 반응(+41%)이 폭발적입니다.<br/>
        • <b>무신사 (Musinsa):</b> 트래픽 킹답게 신상 유입(+67%)을 주도하고 있습니다.<br/>
        • <b>Action Item:</b> 오프라인의 25FW 재고를 온라인으로 이관하고, 자사몰 마케팅 예산을 30% 증액해야 합니다.
        """
        elements.append(Paragraph(summary_text, highlight_box))
        elements.append(PageBreak())

        # ==========================================
        # 2. Macro Performance (Channel & Season)
        # ==========================================
        elements.append(Paragraph("01. 채널 및 시즌별 성과 분석", h1_style))
        elements.append(
            Paragraph(
                "채널별 매출 규모와 시즌별 판매 추이를 분석하여 거시적인 흐름을 파악합니다. 자사몰과 무신사의 신상 성장세가 두드러집니다.",
                body_style,
            )
        )

        # Charts Layout (Stacked if possible, or sequential)
        if "channel_perf" in charts:
            img = Image(charts["channel_perf"], width=170 * mm, height=100 * mm)
            elements.append(img)
            elements.append(Spacer(1, 10 * mm))

        elements.append(Paragraph("<b>📊 성장 모멘텀 분석 (26SS):</b>", body_style))
        if "growth_rate" in charts:
            img = Image(charts["growth_rate"], width=170 * mm, height=80 * mm)
            elements.append(img)

        elements.append(PageBreak())

        # ==========================================
        # 3. Micro Performance (Best Sellers)
        # ==========================================
        elements.append(Paragraph("02. 베스트 셀러 Top 10 분석", h1_style))
        elements.append(
            Paragraph(
                "판매량 상위 10개 품목의 가격 포지셔닝과 매출 기여도를 분석합니다. 고단가 아우터와 회전율이 좋은 이너류의 균형을 확인하세요.",
                body_style,
            )
        )

        if "best_items_scatter" in charts:
            img = Image(charts["best_items_scatter"], width=170 * mm, height=100 * mm)
            elements.append(img)
            elements.append(Spacer(1, 10 * mm))

        # Table Styling (Magazine Style)
        if not micro_data.empty:
            table_data = [
                ["순위", "상품코드 (SKU)", "상품명", "판매가", "판매량", "매출액 (KRW)"]
            ]

            for i, row in micro_data.head(10).iterrows():
                p_name = str(row["Product Name"])
                if len(p_name) > 18:
                    p_name = p_name[:16] + ".."

                table_data.append(
                    [
                        str(i + 1),
                        str(row["SKU"]),
                        p_name,
                        f"{row['Price']:,.0f}",
                        f"{row['Qty']:,.0f}",
                        f"{row['Sales Amount']:,.0f}",
                    ]
                )

            t = Table(
                table_data,
                colWidths=[15 * mm, 35 * mm, 55 * mm, 25 * mm, 20 * mm, 30 * mm],
            )

            t.setStyle(
                TableStyle(
                    [
                        ("FONTNAME", (0, 0), (-1, -1), self.font_name),
                        # Header
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                        ("PADDING", (0, 0), (-1, 0), 10),
                        # Body
                        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#ffffff")),
                        ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#2c3e50")),
                        ("ALIGN", (0, 1), (-1, -1), "CENTER"),
                        ("FONTSIZE", (0, 1), (-1, -1), 9),
                        ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
                        ("TOPPADDING", (0, 1), (-1, -1), 8),
                        # Alternating Row Colors
                        (
                            "ROWBACKGROUNDS",
                            (0, 1),
                            (-1, -1),
                            [colors.HexColor("#f8f9fa"), colors.HexColor("#ffffff")],
                        ),
                        # Lines
                        ("LINEBELOW", (0, 0), (-1, 0), 2, colors.HexColor("#e67e22")),
                        ("LINEBELOW", (0, -1), (-1, -1), 1, colors.HexColor("#bdc3c7")),
                    ]
                )
            )

            elements.append(t)

        # Build PDF
        doc.build(elements)
        print(f"PDF Generated: {self.output_path}")
