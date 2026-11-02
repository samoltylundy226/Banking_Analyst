# Project Plan: Banking Customer Analytics

## Implementation Phases & Progress Checklist

### Phase 1: Data Cleaning & Validation
- [ ] Load `Banking.csv` using `src/data_loader.py` with `encoding='utf-8-sig'`
- [ ] Inspect and resolve 60 duplicated Client IDs
- [ ] Validate minimum age threshold (age = 17)
- [ ] Identify and correct corrupted customer names (e.g., 'Carol GoPKRalez')
- [ ] Parse 'Joined Bank' day-first string dates (dd-mm-yyyy) to datetime format
- [ ] Audit and flag zero balances across deposits, loans, and credit cards
- [ ] Export validated datasets to `data/interim/` and `data/processed/`
- [ ] Write and verify unit tests in `tests/test_cleaning.py`

### Phase 2: Exploratory Data Analysis (EDA)
- [ ] Profile client demographics (Age distribution, Nationalities, Occupations)
- [ ] Analyze wealth and income distributions (Estimated Income vs. Superannuation)
- [ ] Explore Fee Structure and Loyalty Classification segments
- [ ] Examine product cross-holdings (Deposits, Loans, Checking, FX, Credit Cards)
- [ ] Save visual artifacts to `reports/figures/`

### Phase 3: Customer Segmentation
- [ ] Select and scale behavioural and financial attributes
- [ ] Evaluate optimal cluster count (Elbow Method & Silhouette Scores)
- [ ] Train K-Means clustering model in `src/segmentation.py`
- [ ] Build distinct customer personas with actionable business profiles
- [ ] Attach segment labels to processed client data

### Phase 4: Risk and Credit Analysis
- [ ] Examine Risk Weighting distribution (1 to 5) across client segments
- [ ] Assess credit utilization, total loan exposure, and debt ratios
- [ ] Cross-analyze risk weighting against loyalty tier and fee structure
- [ ] Formulate risk mitigation strategies and credit monitoring triggers

### Phase 5: Relationship Manager (RM) Performance
- [ ] Quantify portfolio volume (Total Deposits & Loans) per Banking Contact
- [ ] Analyze client allocation count and workload distribution across RMs
- [ ] Assess cross-sell effectiveness (Credit Cards, FX, Business Lending)
- [ ] Benchmark average client risk rating per RM portfolio

### Phase 6: Dashboard Development
- [ ] Build structured Excel reporting model (`dashboard/excel/`)
- [ ] Design interactive Power BI report (`dashboard/powerbi/`)
- [ ] Configure executive KPI cards, segment slicers, and RM performance drill-downs

### Phase 7: Final Reporting
- [ ] Synthesize findings into `reports/final_report.md`
- [ ] Curate key figures and executive summary for leadership presentation
