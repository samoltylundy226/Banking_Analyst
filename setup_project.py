"""
Setup script for Banking Customer Analytics project.
Creates folder structure, starter files, documentation, notebooks,
virtual environment, and installs project dependencies.
Cross-platform compatible (Windows, macOS, Linux) using pathlib.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def get_project_root() -> Path:
    """Return the base root directory for the banking-analytics project."""
    script_dir = Path(__file__).resolve().parent
    if script_dir.name == "banking-analytics":
        return script_dir
    project_dir = script_dir / "banking-analytics"
    return project_dir if project_dir.exists() else script_dir


def create_directory_structure(root: Path) -> None:
    """Create all required project directories."""
    directories = [
        root / "data" / "raw",
        root / "data" / "interim",
        root / "data" / "processed",
        root / "notebooks",
        root / "src",
        root / "dashboard" / "powerbi",
        root / "dashboard" / "excel",
        root / "reports" / "figures",
        root / "docs",
        root / "tests",
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        gitkeep = directory / ".gitkeep"
        if not any(directory.iterdir()) or not gitkeep.exists():
            if not gitkeep.exists():
                gitkeep.touch()


def make_notebook(title: str, todo_items: list[str] | None = None) -> str:
    """Generate minimal valid Jupyter Notebook JSON with Title and Objectives cells."""
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"# {title}\n"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Objectives\n"]
        }
    ]

    if todo_items:
        todo_lines = ["## Known Issues & To-Do List\n"]
        for item in todo_items:
            todo_lines.append(f"- [ ] {item}\n")
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": todo_lines
        })

    notebook_dict = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    return json.dumps(notebook_dict, indent=1)


def create_starter_files(root: Path) -> None:
    """Create all starter configuration, documentation, source, and notebook files."""
    
    # 1. README.md
    readme_path = root / "README.md"
    if not readme_path.exists():
        readme_path.write_text(
            "# Banking Customer Analytics\n\n"
            "## Project Overview\n"
            "A structured data analytics initiative analyzing 3,000 retail banking clients across 25 demographic, "
            "financial, risk, and relationship dimensions. The project delivers robust data cleaning, exploratory data "
            "analysis (EDA), machine learning-based customer segmentation, credit and risk weighting analysis, "
            "relationship manager (RM) performance benchmarking, and executive dashboards.\n\n"
            "## Folder Structure Overview\n"
            "```text\n"
            "banking-analytics/\n"
            "├── data/\n"
            "│   ├── raw/                 # Original files (read-only, never modified)\n"
            "│   ├── interim/             # Partially transformed / staged data\n"
            "│   └── processed/           # Final cleaned data ready for analysis\n"
            "├── notebooks/\n"
            "│   ├── 01_data_cleaning.ipynb\n"
            "│   ├── 02_eda.ipynb\n"
            "│   ├── 03_segmentation.ipynb\n"
            "│   ├── 04_risk_analysis.ipynb\n"
            "│   └── 05_rm_performance.ipynb\n"
            "├── src/\n"
            "│   ├── __init__.py\n"
            "│   ├── data_loader.py       # Data ingest (load_raw with utf-8-sig)\n"
            "│   ├── cleaning.py          # Data sanitation and validation logic\n"
            "│   ├── features.py          # Feature engineering & transformation\n"
            "│   ├── segmentation.py      # Clustering algorithms and profiling\n"
            "│   └── visualization.py     # Standardized charts and plot styling\n"
            "├── dashboard/\n"
            "│   ├── powerbi/             # Power BI (.pbix) files & assets\n"
            "│   └── excel/               # Excel analytical workbooks & models\n"
            "├── reports/\n"
            "│   ├── figures/             # High-resolution saved plots\n"
            "│   └── final_report.md      # Consolidated analytical findings\n"
            "├── docs/\n"
            "│   ├── data_dictionary.md   # Attribute definitions & data types\n"
            "│   └── project_plan.md      # Phase checklist & execution roadmap\n"
            "├── tests/\n"
            "│   └── test_cleaning.py     # Pytest test cases for cleaning pipeline\n"
            "├── .gitignore               # Git ignore rules for data, envs, cache\n"
            "├── pytest.ini               # Pytest path and runner configuration\n"
            "├── requirements.txt         # Pinned python dependencies\n"
            "├── setup_project.py         # Automated project bootstrap script\n"
            "└── README.md                # Project documentation\n"
            "```\n\n"
            "## How to Run It\n\n"
            "### 1. Environment Setup\n"
            "Ensure Python 3.10+ is installed. Run the bootstrap script to create directories and virtual environment:\n"
            "```bash\n"
            "python setup_project.py\n"
            "```\n\n"
            "### 2. Activate Virtual Environment\n"
            "- **Windows (PowerShell):**\n"
            "  ```powershell\n"
            "  .venv\\Scripts\\Activate.ps1\n"
            "  ```\n"
            "- **macOS / Linux:**\n"
            "  ```bash\n"
            "  source .venv/bin/activate\n"
            "  ```\n\n"
            "### 3. Run Notebooks\n"
            "Launch Jupyter Lab or Notebook:\n"
            "```bash\n"
            "jupyter notebook\n"
            "```\n"
            "Navigate to `notebooks/` and run sequentially from `01_data_cleaning.ipynb` through `05_rm_performance.ipynb`.\n\n"
            "### 4. Run Automated Tests\n"
            "Execute the test suite using pytest:\n"
            "```bash\n"
            "pytest\n"
            "```\n",
            encoding="utf-8"
        )

    # 2. requirements.txt
    req_path = root / "requirements.txt"
    if not req_path.exists():
        req_path.write_text(
            "pandas\n"
            "numpy\n"
            "matplotlib\n"
            "seaborn\n"
            "scikit-learn\n"
            "jupyter\n"
            "openpyxl\n"
            "pytest\n",
            encoding="utf-8"
        )

    # 3. .gitignore
    gitignore_path = root / ".gitignore"
    if not gitignore_path.exists():
        gitignore_path.write_text(
            "# Raw and interim data files\n"
            "data/raw/*\n"
            "!data/raw/.gitkeep\n"
            "data/interim/*\n"
            "!data/interim/.gitkeep\n\n"
            "# Python cache\n"
            "__pycache__/\n"
            "*.py[cod]\n"
            "*$py.class\n"
            ".pytest_cache/\n\n"
            "# Jupyter Checkpoints\n"
            ".ipynb_checkpoints/\n\n"
            "# Virtual Environments & Secrets\n"
            ".venv/\n"
            "venv/\n"
            "env/\n"
            ".env\n",
            encoding="utf-8"
        )

    # 4. pytest.ini
    pytest_ini_path = root / "pytest.ini"
    if not pytest_ini_path.exists():
        pytest_ini_path.write_text(
            "[pytest]\n"
            "pythonpath = .\n"
            "testpaths = tests\n",
            encoding="utf-8"
        )

    # 5. docs/data_dictionary.md
    data_dict_path = root / "docs" / "data_dictionary.md"
    if not data_dict_path.exists():
        data_dict_path.write_text(
            "# Data Dictionary: Banking Customer Dataset\n\n"
            "**Source Dataset:** `Banking.csv`  \n"
            "**Dimensions:** 3,000 client records, 25 columns  \n\n"
            "| Column Name | Description | Data Type |\n"
            "| :--- | :--- | :--- |\n"
            "| Client ID | | String |\n"
            "| Name | | String |\n"
            "| Age | | Integer |\n"
            "| Location ID | | Integer |\n"
            "| Joined Bank | | String (Date dd-mm-yyyy) |\n"
            "| Banking Contact | | String |\n"
            "| Nationality | | String |\n"
            "| Occupation | | String |\n"
            "| Fee Structure | | String (Categorical) |\n"
            "| Loyalty Classification | | String (Categorical) |\n"
            "| Estimated Income | | Float |\n"
            "| Superannuation Savings | | Float |\n"
            "| Amount of Credit Cards | | Integer |\n"
            "| Credit Card Balance | | Float |\n"
            "| Bank Loans | | Float |\n"
            "| Bank Deposits | | Float |\n"
            "| Checking Accounts | | Float |\n"
            "| Saving Accounts | | Float |\n"
            "| Foreign Currency Account | | Float |\n"
            "| Business Lending | | Float |\n"
            "| Properties Owned | | Integer |\n"
            "| Risk Weighting | | Integer |\n"
            "| BRId | coded ID, lookup table not provided | Integer |\n"
            "| GenderId | coded ID, lookup table not provided | Integer |\n"
            "| IAId | coded ID, lookup table not provided | Integer |\n",
            encoding="utf-8"
        )

    # 6. docs/project_plan.md
    project_plan_path = root / "docs" / "project_plan.md"
    if not project_plan_path.exists():
        project_plan_path.write_text(
            "# Project Plan: Banking Customer Analytics\n\n"
            "## Implementation Phases & Progress Checklist\n\n"
            "### Phase 1: Data Cleaning & Validation\n"
            "- [ ] Load `Banking.csv` using `src/data_loader.py` with `encoding='utf-8-sig'`\n"
            "- [ ] Inspect and resolve 60 duplicated Client IDs\n"
            "- [ ] Validate minimum age threshold (age = 17)\n"
            "- [ ] Identify and correct corrupted customer names (e.g., 'Carol GoPKRalez')\n"
            "- [ ] Parse 'Joined Bank' day-first string dates (dd-mm-yyyy) to datetime format\n"
            "- [ ] Audit and flag zero balances across deposits, loans, and credit cards\n"
            "- [ ] Export validated datasets to `data/interim/` and `data/processed/`\n"
            "- [ ] Write and verify unit tests in `tests/test_cleaning.py`\n\n"
            "### Phase 2: Exploratory Data Analysis (EDA)\n"
            "- [ ] Profile client demographics (Age distribution, Nationalities, Occupations)\n"
            "- [ ] Analyze wealth and income distributions (Estimated Income vs. Superannuation)\n"
            "- [ ] Explore Fee Structure and Loyalty Classification segments\n"
            "- [ ] Examine product cross-holdings (Deposits, Loans, Checking, FX, Credit Cards)\n"
            "- [ ] Save visual artifacts to `reports/figures/`\n\n"
            "### Phase 3: Customer Segmentation\n"
            "- [ ] Select and scale behavioural and financial attributes\n"
            "- [ ] Evaluate optimal cluster count (Elbow Method & Silhouette Scores)\n"
            "- [ ] Train K-Means clustering model in `src/segmentation.py`\n"
            "- [ ] Build distinct customer personas with actionable business profiles\n"
            "- [ ] Attach segment labels to processed client data\n\n"
            "### Phase 4: Risk and Credit Analysis\n"
            "- [ ] Examine Risk Weighting distribution (1 to 5) across client segments\n"
            "- [ ] Assess credit utilization, total loan exposure, and debt ratios\n"
            "- [ ] Cross-analyze risk weighting against loyalty tier and fee structure\n"
            "- [ ] Formulate risk mitigation strategies and credit monitoring triggers\n\n"
            "### Phase 5: Relationship Manager (RM) Performance\n"
            "- [ ] Quantify portfolio volume (Total Deposits & Loans) per Banking Contact\n"
            "- [ ] Analyze client allocation count and workload distribution across RMs\n"
            "- [ ] Assess cross-sell effectiveness (Credit Cards, FX, Business Lending)\n"
            "- [ ] Benchmark average client risk rating per RM portfolio\n\n"
            "### Phase 6: Dashboard Development\n"
            "- [ ] Build structured Excel reporting model (`dashboard/excel/`)\n"
            "- [ ] Design interactive Power BI report (`dashboard/powerbi/`)\n"
            "- [ ] Configure executive KPI cards, segment slicers, and RM performance drill-downs\n\n"
            "### Phase 7: Final Reporting\n"
            "- [ ] Synthesize findings into `reports/final_report.md`\n"
            "- [ ] Curate key figures and executive summary for leadership presentation\n",
            encoding="utf-8"
        )

    # 7. reports/final_report.md
    report_path = root / "reports" / "final_report.md"
    if not report_path.exists():
        report_path.write_text(
            "# Banking Customer Analytics: Final Report\n\n"
            "## Executive Summary\n"
            "*(Summary of strategic findings and analytical conclusions to be completed upon project execution)*\n\n"
            "## 1. Project Background\n"
            "Analysis of 3,000 retail banking clients across 25 features to uncover customer value drivers, "
            "underwrite risk effectively, and benchmark relationship manager efficiency.\n\n"
            "## 2. Data Cleaning & Integrity Audit\n"
            "- Deduplication findings (60 duplicated Client IDs)\n"
            "- Demographic integrity checks (Age 17 threshold, name corruption fix)\n"
            "- Date normalization (dd-mm-yyyy)\n"
            "- Zero-balance account treatment\n\n"
            "## 3. Exploratory Data Analysis & Customer Demographics\n"
            "- Income & deposit distribution patterns\n"
            "- Loyalty tier and fee structure dynamics\n\n"
            "## 4. Customer Segmentation Personas\n"
            "- Cluster methodology and profiles\n"
            "- Targeted growth strategies per segment\n\n"
            "## 5. Credit & Risk Assessment\n"
            "- Risk weighting distribution and loan exposures\n"
            "- Vulnerability identification\n\n"
            "## 6. Relationship Manager Performance\n"
            "- Portfolio volume and revenue contributions\n"
            "- Cross-sell depth and workload equity\n\n"
            "## 7. Actionable Recommendations\n"
            "- Commercial and operational action plan\n",
            encoding="utf-8"
        )

    # 8. src/__init__.py
    init_path = root / "src" / "__init__.py"
    if not init_path.exists():
        init_path.write_text(
            '"""\n'
            'Banking Customer Analytics Package.\n\n'
            'Provides modules for loading, cleaning, feature engineering,\n'
            'segmenting, and visualizing retail banking client portfolios.\n'
            '"""\n\n'
            '__version__ = "0.1.0"\n',
            encoding="utf-8"
        )

    # 9. src/data_loader.py
    data_loader_path = root / "src" / "data_loader.py"
    if not data_loader_path.exists():
        data_loader_path.write_text(
            '"""\n'
            'Data loading utilities for Banking Customer Analytics.\n\n'
            'Provides functions to load raw, interim, and processed data assets.\n'
            '"""\n\n'
            'from pathlib import Path\n'
            'from typing import Optional, Union\n'
            'import pandas as pd\n\n\n'
            'def load_raw(filepath: Optional[Union[Path, str]] = None) -> pd.DataFrame:\n'
            '    """\n'
            '    Load raw Banking.csv dataset with utf-8-sig encoding.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    filepath : Path or str, optional\n'
            '        Path to Banking.csv file. If None, defaults to data/raw/Banking.csv\n'
            '        relative to the project root directory.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Raw customer dataframe loaded with utf-8-sig encoding.\n'
            '    """\n'
            '    if filepath is None:\n'
            '        filepath = Path(__file__).resolve().parent.parent / "data" / "raw" / "Banking.csv"\n'
            '    return pd.read_csv(filepath, encoding="utf-8-sig")\n\n\n'
            'def load_interim(filepath: Optional[Union[Path, str]] = None) -> pd.DataFrame:\n'
            '    """\n'
            '    Load interim (partially cleaned) dataset.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    filepath : Path or str, optional\n'
            '        Path to interim CSV file.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Interim customer dataframe.\n'
            '    """\n'
            '    pass\n\n\n'
            'def load_processed(filepath: Optional[Union[Path, str]] = None) -> pd.DataFrame:\n'
            '    """\n'
            '    Load final cleaned and validated dataset ready for analysis.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    filepath : Path or str, optional\n'
            '        Path to processed CSV file.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Processed customer analytics dataframe.\n'
            '    """\n'
            '    pass\n',
            encoding="utf-8"
        )

    # 10. src/cleaning.py
    cleaning_path = root / "src" / "cleaning.py"
    if not cleaning_path.exists():
        cleaning_path.write_text(
            '"""\n'
            'Data cleaning and validation module for Banking Customer Analytics.\n\n'
            'Handles deduplication of Client IDs, name anomaly correction,\n'
            'day-first date parsing, demographic boundary validation, and zero-balance treatment.\n'
            '"""\n\n'
            'from typing import Tuple\n'
            'import pandas as pd\n\n\n'
            'def remove_duplicate_clients(df: pd.DataFrame) -> pd.DataFrame:\n'
            '    """\n'
            '    Identify and resolve duplicated Client IDs in the dataset.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Raw banking dataframe.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Deduplicated dataframe.\n'
            '    """\n'
            '    pass\n\n\n'
            'def clean_names(df: pd.DataFrame, name_col: str = "Name") -> pd.DataFrame:\n'
            '    """\n'
            '    Detect and correct corrupted characters or encoding glitches in client names.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n'
            '    name_col : str, default "Name"\n'
            '        Name column to sanitize.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe with cleaned name strings.\n'
            '    """\n'
            '    pass\n\n\n'
            'def parse_dates(df: pd.DataFrame, date_col: str = "Joined Bank") -> pd.DataFrame:\n'
            '    """\n'
            '    Parse day-first string dates (dd-mm-yyyy) into datetime objects.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n'
            '    date_col : str, default "Joined Bank"\n'
            '        Column containing day-first date strings.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe with converted datetime column.\n'
            '    """\n'
            '    pass\n\n\n'
            'def validate_demographics(df: pd.DataFrame, min_age: int = 17) -> pd.DataFrame:\n'
            '    """\n'
            '    Validate demographic boundaries including client age and identity codes.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n'
            '    min_age : int, default 17\n'
            '        Minimum age threshold to evaluate.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe with validated demographic records.\n'
            '    """\n'
            '    pass\n\n\n'
            'def handle_zero_balances(df: pd.DataFrame) -> pd.DataFrame:\n'
            '    """\n'
            '    Inspect and flag zero balances across deposits, loans, and credit cards.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe with categorized balance indicators.\n'
            '    """\n'
            '    pass\n\n\n'
            'def run_cleaning_pipeline(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:\n'
            '    """\n'
            '    Execute comprehensive cleaning pipeline and generate validation audit metrics.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Raw customer dataframe.\n\n'
            '    Returns\n'
            '    -------\n'
            '    Tuple[pd.DataFrame, dict]\n'
            '        Cleaned dataframe and summary dictionary of applied corrections.\n'
            '    """\n'
            '    pass\n',
            encoding="utf-8"
        )

    # 11. src/features.py
    features_path = root / "src" / "features.py"
    if not features_path.exists():
        features_path.write_text(
            '"""\n'
            'Feature engineering module for Banking Customer Analytics.\n\n'
            'Calculates customer relationship tenure, aggregated balances, debt ratios,\n'
            'and financial vulnerability indicators.\n'
            '"""\n\n'
            'from typing import List\n'
            'import pandas as pd\n\n\n'
            'def calculate_tenure(df: pd.DataFrame, date_col: str = "Joined Bank") -> pd.DataFrame:\n'
            '    """\n'
            '    Calculate customer relationship tenure in months and years.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Cleaned banking dataframe.\n'
            '    date_col : str, default "Joined Bank"\n'
            '        Name of datetime column.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe enriched with tenure columns.\n'
            '    """\n'
            '    pass\n\n\n'
            'def calculate_total_balance(df: pd.DataFrame) -> pd.DataFrame:\n'
            '    """\n'
            '    Aggregate total client balance across deposits, savings, checking, and FX accounts.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe with total balance and asset columns.\n'
            '    """\n'
            '    pass\n\n\n'
            'def calculate_credit_utilization(df: pd.DataFrame) -> pd.DataFrame:\n'
            '    """\n'
            '    Calculate credit card utilization metrics and loan-to-income ratios.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Dataframe with leverage and exposure ratios.\n'
            '    """\n'
            '    pass\n\n\n'
            'def build_feature_set(df: pd.DataFrame) -> pd.DataFrame:\n'
            '    """\n'
            '    Execute complete feature engineering pipeline for segmentation and risk modeling.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Cleaned customer dataframe.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Enriched dataframe with all engineered analytical features.\n'
            '    """\n'
            '    pass\n',
            encoding="utf-8"
        )

    # 12. src/segmentation.py
    segmentation_path = root / "src" / "segmentation.py"
    if not segmentation_path.exists():
        segmentation_path.write_text(
            '"""\n'
            'Customer segmentation module for Banking Customer Analytics.\n\n'
            'Provides preprocessing, feature scaling, K-Means clustering, and segment profiling.\n'
            '"""\n\n'
            'from typing import Dict, List, Tuple\n'
            'import pandas as pd\n\n\n'
            'def prepare_cluster_matrix(\n'
            '    df: pd.DataFrame, features: List[str]\n'
            ') -> Tuple[pd.DataFrame, object]:\n'
            '    """\n'
            '    Scale and normalize selected numerical features for clustering models.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Dataframe containing analytical features.\n'
            '    features : List[str]\n'
            '        Columns to include in clustering.\n\n'
            '    Returns\n'
            '    -------\n'
            '    Tuple[pd.DataFrame, object]\n'
            '        Standardized feature matrix and fitted scaler object.\n'
            '    """\n'
            '    pass\n\n\n'
            'def evaluate_cluster_range(\n'
            '    matrix: pd.DataFrame, k_range: range = range(2, 9)\n'
            ') -> Dict[str, List[float]]:\n'
            '    """\n'
            '    Evaluate K-Means performance across k values using inertia and silhouette scores.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    matrix : pd.DataFrame\n'
            '        Scaled clustering matrix.\n'
            '    k_range : range, default range(2, 9)\n'
            '        Cluster range to evaluate.\n\n'
            '    Returns\n'
            '    -------\n'
            '    Dict[str, List[float]]\n'
            '        Dictionary of inertia and silhouette evaluation scores.\n'
            '    """\n'
            '    pass\n\n\n'
            'def train_kmeans(\n'
            '    matrix: pd.DataFrame, n_clusters: int = 4, random_state: int = 42\n'
            ') -> Tuple[pd.Series, object]:\n'
            '    """\n'
            '    Train K-Means clustering model and assign segment labels.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    matrix : pd.DataFrame\n'
            '        Scaled clustering matrix.\n'
            '    n_clusters : int, default 4\n'
            '        Number of target clusters.\n'
            '    random_state : int, default 42\n'
            '        Random seed.\n\n'
            '    Returns\n'
            '    -------\n'
            '    Tuple[pd.Series, object]\n'
            '        Cluster label series and fitted KMeans model.\n'
            '    """\n'
            '    pass\n\n\n'
            'def profile_clusters(df: pd.DataFrame, cluster_col: str = "Cluster") -> pd.DataFrame:\n'
            '    """\n'
            '    Compute demographic and financial profiles for each customer segment.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Dataframe with segment assignments.\n'
            '    cluster_col : str, default "Cluster"\n'
            '        Cluster label column name.\n\n'
            '    Returns\n'
            '    -------\n'
            '    pd.DataFrame\n'
            '        Segment summary profile table.\n'
            '    """\n'
            '    pass\n',
            encoding="utf-8"
        )

    # 13. src/visualization.py
    visualization_path = root / "src" / "visualization.py"
    if not visualization_path.exists():
        visualization_path.write_text(
            '"""\n'
            'Visualization styling and plotting utilities for Banking Customer Analytics.\n\n'
            'Provides chart styling and standardized plotting routines for EDA,\n'
            'segmentation, risk analysis, and relationship manager scorecards.\n'
            '"""\n\n'
            'from typing import Optional, Union\n'
            'from pathlib import Path\n'
            'import matplotlib.pyplot as plt\n'
            'import pandas as pd\n\n\n'
            'def set_visual_theme() -> None:\n'
            '    """\n'
            '    Apply uniform matplotlib and seaborn styling rules and corporate color palettes.\n'
            '    """\n'
            '    pass\n\n\n'
            'def plot_demographics(\n'
            '    df: pd.DataFrame, save_path: Optional[Union[Path, str]] = None\n'
            ') -> plt.Figure:\n'
            '    """\n'
            '    Plot distribution of client demographics (Age, Nationality, Occupation).\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Cleaned customer dataset.\n'
            '    save_path : Path or str, optional\n'
            '        Filepath to save figure.\n\n'
            '    Returns\n'
            '    -------\n'
            '    plt.Figure\n'
            '        Matplotlib Figure object.\n'
            '    """\n'
            '    pass\n\n\n'
            'def plot_risk_distribution(\n'
            '    df: pd.DataFrame, save_path: Optional[Union[Path, str]] = None\n'
            ') -> plt.Figure:\n'
            '    """\n'
            '    Plot risk weighting distribution cross-tabulated with loan balances.\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n'
            '    save_path : Path or str, optional\n'
            '        Filepath to save figure.\n\n'
            '    Returns\n'
            '    -------\n'
            '    plt.Figure\n'
            '        Matplotlib Figure object.\n'
            '    """\n'
            '    pass\n\n\n'
            'def plot_rm_performance(\n'
            '    df: pd.DataFrame, save_path: Optional[Union[Path, str]] = None\n'
            ') -> plt.Figure:\n'
            '    """\n'
            '    Plot portfolio assets and client count per Banking Contact (Relationship Manager).\n\n'
            '    Parameters\n'
            '    ----------\n'
            '    df : pd.DataFrame\n'
            '        Banking dataframe.\n'
            '    save_path : Path or str, optional\n'
            '        Filepath to save figure.\n\n'
            '    Returns\n'
            '    -------\n'
            '    plt.Figure\n'
            '        Matplotlib Figure object.\n'
            '    """\n'
            '    pass\n',
            encoding="utf-8"
        )

    # 14. tests/test_cleaning.py
    test_path = root / "tests" / "test_cleaning.py"
    if not test_path.exists():
        test_path.write_text(
            '"""\n'
            'Unit tests for data cleaning logic in Banking Customer Analytics.\n'
            '"""\n\n'
            'import pytest\n'
            'import pandas as pd\n'
            'from src.cleaning import (\n'
            '    remove_duplicate_clients,\n'
            '    clean_names,\n'
            '    parse_dates,\n'
            '    validate_demographics,\n'
            '    handle_zero_balances,\n'
            ')\n\n\n'
            '@pytest.fixture\n'
            'def sample_raw_banking_df() -> pd.DataFrame:\n'
            '    """Provide minimal mock dataframe reflecting known anomalies."""\n'
            '    return pd.DataFrame({\n'
            '        "Client ID": ["IND81288", "IND81288", "IND65833", "IND47499"],\n'
            '        "Name": ["Raymond Mills", "Raymond Mills", "Carol GoPKRalez", "Stephen Murray"],\n'
            '        "Age": [24, 24, 17, 27],\n'
            '        "Joined Bank": ["06-05-2019", "06-05-2019", "10-12-2001", "25-01-2010"],\n'
            '        "Bank Deposits": [1485828.64, 1485828.64, 0.0, 1033401.59],\n'
            '        "Bank Loans": [776242.92, 776242.92, 1270615.43, 0.0],\n'
            '        "Credit Card Balance": [484.54, 484.54, 0.0, 4568.74],\n'
            '    })\n\n\n'
            'def test_remove_duplicate_clients_stub():\n'
            '    """Verify duplicate removal function stub is callable."""\n'
            '    pass\n\n\n'
            'def test_clean_names_stub():\n'
            '    """Verify corrupted name cleaning function stub is callable."""\n'
            '    pass\n\n\n'
            'def test_parse_dates_stub():\n'
            '    """Verify day-first date parser function stub is callable."""\n'
            '    pass\n\n\n'
            'def test_validate_demographics_stub():\n'
            '    """Verify demographic boundary check function stub is callable."""\n'
            '    pass\n\n\n'
            'def test_handle_zero_balances_stub():\n'
            '    """Verify zero balance handler function stub is callable."""\n'
            '    pass\n',
            encoding="utf-8"
        )

    # 15. notebooks
    known_issues = [
        "60 duplicated Client IDs",
        "minimum age is 17",
        "possible corrupted names (e.g. \"Carol GoPKRalez\")",
        "Joined Bank is a day-first text date (dd-mm-yyyy)",
        "zero balances in some accounts"
    ]

    notebook_configs = [
        ("01_data_cleaning.ipynb", "01 - Data Cleaning & Validation", known_issues),
        ("02_eda.ipynb", "02 - Exploratory Data Analysis (EDA)", None),
        ("03_segmentation.ipynb", "03 - Customer Segmentation", None),
        ("04_risk_analysis.ipynb", "04 - Risk & Credit Analysis", None),
        ("05_rm_performance.ipynb", "05 - Relationship Manager Performance", None),
    ]

    for filename, title, issues in notebook_configs:
        nb_path = root / "notebooks" / filename
        if not nb_path.exists():
            nb_path.write_text(make_notebook(title, issues), encoding="utf-8")


def move_banking_dataset(root: Path) -> bool:
    """
    Search for Banking.csv in workspace or user downloads and place it in data/raw/.
    Preserves original download file by copying if external to avoid unintended data loss.
    """
    dest = root / "data" / "raw" / "Banking.csv"
    if dest.exists():
        return True

    # Search candidates
    search_locations = [
        root / "Banking.csv",
        root.parent / "Banking.csv",
        Path.cwd() / "Banking.csv",
        Path.home() / "Downloads" / "Banking.csv",
    ]

    for candidate in search_locations:
        if candidate.exists() and candidate.is_file():
            shutil.copy2(candidate, dest)
            return True

    return False


def setup_virtual_environment(root: Path) -> None:
    """Create .venv and install requirements.txt."""
    venv_dir = root / ".venv"
    req_file = root / "requirements.txt"

    uv_path = shutil.which("uv")
    if uv_path:
        print(f"Using uv at {uv_path} to create virtual environment and install packages...")
        if not venv_dir.exists():
            subprocess.run([uv_path, "venv", str(venv_dir), "--python", "3.12"], check=True)
        if req_file.exists():
            subprocess.run([uv_path, "pip", "install", "-r", str(req_file), "--python", str(venv_dir)], check=True)
    else:
        print("Using standard python venv...")
        if not venv_dir.exists():
            subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
        pip_exe = venv_dir / ("Scripts" if os.name == "nt" else "bin") / ("pip.exe" if os.name == "nt" else "pip")
        if req_file.exists():
            subprocess.run([str(pip_exe), "install", "-r", str(req_file)], check=True)


def main() -> None:
    """Main execution function."""
    root = get_project_root()
    print(f"Setting up Banking Customer Analytics project at: {root}")
    create_directory_structure(root)
    create_starter_files(root)
    found = move_banking_dataset(root)
    if found:
        print(f"Dataset successfully placed in: {root / 'data' / 'raw' / 'Banking.csv'}")
    else:
        print("Note: Banking.csv was not found in common workspace locations.")
    setup_virtual_environment(root)
    print("Project workspace setup completed successfully!")


if __name__ == "__main__":
    main()
