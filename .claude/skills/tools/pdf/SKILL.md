---
name: pdf
description: 패션 비즈니스 리포트 및 룩북 PDF 제작 도구
version: 2.0.0
author: Wacky Willy Fashion House
tags:
  - pdf
  - document
  - fashion
  - report
---

# Fashion PDF Toolkit

패션 비즈니스에 필요한 **트렌드 리포트, 룩북(Lookbook), 작업지시서(Tech Pack)**를 PDF로 생성하고 처리하는 도구입니다.

## 주요 기능 (Fashion Context)

| 기능 | 설명 | 용도 |
|------|------|------|
| **Tech Pack 생성** | Markdown → PDF | 공장 전달용 작업지시서 생성 |
| **Lookbook 병합** | 이미지 + 텍스트 병합 | 바이어 전달용 시즌 룩북 패키징 |
| **Competitor Parsing** | 경쟁사 PDF 리포트 분석 | 텍스트/테이블 데이터 추출 |

## Workflow Example: Tech Pack Generation

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Image

def create_tech_pack(data, output_path):
    """
    작업지시서(Tech Pack) PDF 생성
    data: {item_name, bom_table, size_spec, sketch_image}
    """
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []
    
    # 1. 도식화 (Flat Sketch)
    elements.append(Image(data['sketch_image'], width=400, height=300))
    
    # 2. BOM Table
    elements.append(Table(data['bom_table']))
    
    # 3. Size Spec
    elements.append(Table(data['size_spec']))
    
    doc.build(elements)
```

## File Storage (Naming Convention)

*   **Tech Pack**: `reports/pdf/techpack-{season}-{item_code}.pdf`
    *   Example: `techpack-26ss-hoodie-01.pdf`
*   **Lookbook**: `reports/pdf/lookbook-{season}.pdf`
    *   Example: `lookbook-26ss-wacky-chaos.pdf`

## Usage
이 스킬은 `production-manager`가 작업지시서 발행 시, `marketing-director`가 룩북 배포 시 사용합니다.
