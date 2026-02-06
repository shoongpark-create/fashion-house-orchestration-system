# Techpack Generator Skill (테크팩 생성)

## Overview
디자인 시안을 기반으로 생산 가능한 기술 문서(Tech Pack)를 생성하는 스킬입니다.

## Trigger
- 디자인 승인 후 생산 준비 단계
- `/create-techpack` 커맨드 실행 시

## Inputs
| 항목 | 설명 | 필수 |
|------|------|------|
| `design_path` | 승인된 디자인 시안 경로 | ✅ |
| `item_name` | 상품명 | ✅ |
| `season` | 시즌 코드 (예: 26SS) | ✅ |
| `category` | 카테고리 (TOP/BOTTOM/OUTER/ACC) | ✅ |
| `size_range` | 사이즈 범위 | ✅ |

## Tech Pack Structure

### 1. Cover Page
- 스타일 번호, 시즌, 디자이너
- 승인 일자, 버전 히스토리

### 2. Design Specification
- 도식화 (Front/Back/Detail)
- 컬러웨이 (Pantone 코드)
- 디자인 포인트 설명

### 3. Bill of Materials (BOM)
| Component | Material | Supplier | Color | Quantity | Unit Price |
|-----------|----------|----------|-------|----------|------------|
| Shell | Cotton Twill | A사 | Black | 1.2m | ₩8,000 |
| Lining | Poly Taffeta | B사 | Black | 0.8m | ₩3,500 |
| Zipper | YKK #5 | YKK | Silver | 1ea | ₩1,200 |

### 4. Size Specification
| POM | S | M | L | XL | Tolerance |
|-----|---|---|---|----|-----------|
| Chest | 54 | 57 | 60 | 63 | ±1.0 |
| Length | 68 | 70 | 72 | 74 | ±1.0 |
| Shoulder | 44 | 46 | 48 | 50 | ±0.5 |

### 5. Construction Details
- 봉제 사양 (스티치 종류, SPI)
- 심지 부착 위치
- 후가공 지시 (워싱, 프린트 등)

### 6. Label & Packaging
- 메인라벨, 케어라벨, 사이즈라벨
- 행택, 폴리백, 박스 사양

## Outputs
```
03_Product/Drops/{delivery_folder}/
├── TechPack_{item_name}.md      # 메인 테크팩
├── BOM_{item_name}.csv          # 자재 명세
├── Size_Spec_{item_name}.csv    # 치수 스펙
└── assets/
    ├── flat_front.png           # 도식화
    ├── flat_back.png
    └── detail_views/
```

## Rules
- 스펙 동결(Spec Lock) 후 변경 시 전체 승인 필요
- 모든 치수는 cm 단위, 소수점 1자리
- Pantone 코드 필수 명시 (CMYK/RGB 보조)
- 버전 관리: v1.0, v1.1, v2.0 형식

## Validation Checklist
- [ ] 모든 자재에 공급업체 명시
- [ ] 사이즈별 그레이딩 규칙 일관성
- [ ] 케어라벨 세탁 기호 정확성
- [ ] 원산지 표기 확인

## Related Skills
- `product/costing`: BOM 기반 원가 산출
- `product/qc-checklist`: 스펙 기준 QC 연동
- `creative/kie-image-generator`: 도식화 이미지 생성
