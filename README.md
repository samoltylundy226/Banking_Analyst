# Banking Customer Analytics

## Project Overview
A structured data analytics initiative analyzing 3,000 retail banking clients across 25 demographic, financial, risk, and relationship dimensions. The project delivers robust data cleaning, exploratory data analysis (EDA), machine learning-based customer segmentation, credit and risk weighting analysis, relationship manager (RM) performance benchmarking, and executive dashboards.

## Folder Structure Overview
```text
banking-analytics/
├── data/
│   ├── raw/                 # Original files (read-only, never modified)
│   ├── interim/             # Partially transformed / staged data
│   └── processed/           # Final cleaned data ready for analysis
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_segmentation.ipynb
│   ├── 04_risk_analysis.ipynb
│   └── 05_rm_performance.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py       # Data ingest (load_raw with utf-8-sig)
│   ├── cleaning.py          # Data sanitation and validation logic
│   ├── features.py          # Feature engineering & transformation
│   ├── segmentation.py      # Clustering algorithms and profiling
│   └── visualization.py     # Standardized charts and plot styling
├── dashboard/
│   ├── powerbi/             # Power BI (.pbix) files & assets
│   └── excel/               # Excel analytical workbooks & models
├── reports/
│   ├── figures/             # High-resolution saved plots
│   └── final_report.md      # Consolidated analytical findings
├── docs/
│   ├── data_dictionary.md   # Attribute definitions & data types
│   └── project_plan.md      # Phase checklist & execution roadmap
├── tests/
│   └── test_cleaning.py     # Pytest test cases for cleaning pipeline
├── .gitignore               # Git ignore rules for data, envs, cache
├── requirements.txt         # Pinned python dependencies
├── setup_project.py         # Automated project bootstrap script
└── README.md                # Project documentation
```

## How to Run It

### 1. Environment Setup
Ensure Python 3.10+ is installed. Run the bootstrap script to create directories and virtual environment:
```bash
python setup_project.py
```

### 2. Activate Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Run Notebooks
Launch Jupyter Lab or Notebook:
```bash
jupyter notebook
```
Navigate to `notebooks/` and run sequentially from `01_data_cleaning.ipynb` through `05_rm_performance.ipynb`.

### 4. Run Automated Tests
Execute the test suite using pytest:
```bash
pytest
```
