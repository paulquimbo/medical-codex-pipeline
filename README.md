# Medical Codex Pipeline

## Project Description

This is a school project designed to simulate the responsibilities of a data scientist working in the healthcare software industry. The goal is to build a robust data pipeline that processes and maintains standardized reference datasets for various medical codexes. These codexes are essential for healthcare applications and must be kept accurate and up-to-date.

The pipeline will ingest raw data files, clean and validate the contents, and convert them into standardized CSV format suitable for production use.

## Key Competencies Demonstrated

This project showcases practical proficiency in:

- Understanding and working with healthcare data standards  
- Designing and implementing ETL pipelines using Python  
- Validating and cleaning complex datasets for accuracy  
- Optimizing file formats for efficient storage and processing  
- Writing modular, maintainable, and production-style code


## 🛠️ What Was Done

Python scripts were developed to process each medical codex listed below. For every codex, the following steps were completed:

- Ingested raw codex data from various formats  
- Cleaned and validated the data to ensure consistency and accuracy  
- Converted the datasets into standardized CSV format  
- Saved the final outputs in a structured directory for downstream use


## Target Medical Codexes

Based on the company’s `about.md` reference document, the following codexes will be processed:

1. **SNOMED CT (US)** – Clinical terminology  
2. **ICD-10-CM (US)** – Diagnosis codes  
3. **ICD-10 (WHO)** – International diagnosis codes  
4. **HCPCS (US)** – Healthcare procedure codes  
5. **LOINC (US)** – Laboratory test codes  
6. **RxNorm (US)** – Medication codes  
7. **NPI (US)** – Healthcare provider identifiers  

## 📤 Expected Output

For each codex, the pipeline will generate:

- A cleaned and validated CSV file stored in the `output/csv/` directory  
- Logs or messages indicating any data issues or validation errors  
- Modular Python scripts located in the `scripts/` directory  
- Shared utility functions in `utils/common_functions.py`  

---

This project emphasizes clean code, modular design, and real-world data engineering practices. It’s a great opportunity to build practical skills while working with healthcare data standards.
