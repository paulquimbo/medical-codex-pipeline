# Medical Codex Pipeline

## Project Overview

This school project simulates the role of a data scientist in the healthcare software industry. The goal is to build a robust, modular data pipeline that processes and maintains standardized reference datasets for various medical codexes. These codexes are critical for healthcare applications and must be kept accurate and up-to-date.

The pipeline ingests raw data files, cleans and validates their contents, and converts them into standardized CSV format suitable for production use.

> This project is developed using [Visual Studio Code](https://code.visualstudio.com/) for efficient scripting, debugging, and workflow management.

## Key Competencies Demonstrated

This project showcases practical proficiency in:

- Working with healthcare data standards and formats  
- Designing ETL pipelines using Python  
- Validating and cleaning complex datasets  
- Optimizing file formats for efficient storage and processing  
- Writing modular, maintainable, and production-grade code  

## What Was Built

Python scripts were developed to process each medical codex listed below. For every codex, the pipeline performs:

- Ingestion of raw data from various formats  
- Cleaning and validation for consistency and accuracy  
- Conversion to standardized CSV format  
- Saving outputs in a structured directory for downstream use  

## Codexes Processed and Reference Data Sources

| Codex Name         | Description                        | Source Link |
|--------------------|------------------------------------|-------------|
| SNOMED CT (US)     | Clinical terminology               | [SNOMED Archive](https://www.nlm.nih.gov/healthit/snomedct/archive.html) |
| ICD-10-CM (US)     | Diagnosis codes                    | [CMS ICD-10-CM](https://www.cms.gov/medicare/coding-billing/icd-10-codes) |
| ICD-10 (WHO)       | International diagnosis codes      | [WHO ICD-10](https://icdcdn.who.int/icd10/index.html) |
| HCPCS (US)         | Healthcare procedure codes         | [CMS HCPCS Update](https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update) |
| LOINC (US)         | Laboratory test codes              | [LOINC Downloads](https://loinc.org/downloads/) |
| RxNorm (US)        | Medication codes                   | [RxNorm Files](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html) |
| NPI (US)           | Provider identifiers               | [NPI Registry Files](https://download.cms.gov/nppes/NPI_Files.html) |

---

## Setup Instructions

To get started with the Medical Codex Pipeline:

### Step 1: Clone the repository

```bash
git clone https://github.com/paulquimbo/medical-codex-pipeline.git
cd medical-codex-pipeline
```

### Step 2: Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Run codex-specific scripts

```bash
python scripts/process_rxnorm.py
python scripts/process_snomed.py
```

---

## Usage Examples

### Process SNOMED CT

```bash
python scripts/process_snomed.py
```

### Save a cleaned DataFrame

```python
from utils.common_functions import save_to_csv

save_to_csv(df, "snomed_cleaned.csv")
```

---

## Output Structure

Each codex script generates:

- A cleaned CSV file in `output/csv/`
- Logs indicating validation issues
- Modular scripts in `scripts/`
- Shared utilities in `utils/common_functions.py`

---

## Notes

This project emphasizes clean code, modular design, and real-world data engineering practices. It’s a hands-on opportunity to build practical skills while working with healthcare data standards.
