# 📊 Data & AI Job Market Analysis

**End-to-end exploratory data analysis of global Data & AI job postings — uncovering salary trends, remote work patterns, and market dynamics across roles, experience levels, and geographies.**

---

## 🎯 Objectives

- Analyze salary distributions across Data & AI roles worldwide
- Identify key factors driving compensation (experience, company size, location, remote work)
- Detect statistically significant differences between experience groups
- Produce publication-quality visualizations that tell a clear story

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| pandas | Data manipulation & cleaning |
| seaborn / matplotlib | Statistical visualizations |
| scipy | Hypothesis testing (ANOVA, Tukey HSD) |
| Jupyter Notebook | Interactive analysis |

## 📁 Project Structure

```
data-ai-jobs-analysis/
├── data/
│   ├── raw/                # Original dataset
│   └── processed/          # Cleaned & transformed data
├── notebooks/
│   └── 01_eda.ipynb        # Exploratory Data Analysis
├── src/
│   ├── __init__.py
│   ├── clean.py            # Data loading & cleaning pipeline
│   ├── features.py         # Feature engineering utilities
│   └── visualize.py        # Reusable chart functions
├── outputs/
│   └── figures/            # Saved visualizations
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/FranciscoMartinezGrecco/Data-ai-jobs-analysis.git
cd Data-ai-jobs-analysis

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook notebooks/01_eda.ipynb
```

## 📈 Key Findings

> *Coming soon — analysis in progress.*

## 📊 Dataset

- **Source:** [Kaggle — Data Science Job Salaries](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)
- **Records:** 607 job postings
- **Period:** 2020–2022
- **Features:** job title, experience level, employment type, salary (USD), remote ratio, company size, company location, employee residence

## 👤 Author

**Francisco Martinez Grecco**
Data Science Student @ UNSAM
- GitHub: [@FranciscoMartinezGrecco](https://github.com/FranciscoMartinezGrecco)
