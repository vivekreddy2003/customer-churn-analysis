# 📊 Customer Churn Analysis - Telecom Industry

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive data analysis project that identifies factors driving customer churn in the telecom industry and provides actionable business insights.

![Dashboard Preview](visualizations/07_dashboard.png)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Findings](#-key-findings)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Analysis Components](#-analysis-components)
- [Visualizations](#-visualizations)
- [Business Recommendations](#-business-recommendations)
- [SQL Queries](#-sql-queries)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🎯 Project Overview

### Business Problem
Customer churn is a critical challenge for telecom companies. Acquiring new customers costs **5-7x more** than retaining existing ones. This project analyzes customer data to:

- Identify key factors driving customer churn
- Quantify revenue impact of customer attrition
- Develop data-driven retention strategies
- Create actionable business recommendations

### Dataset
- **100+ customers** with 21 features
- Features include demographics, services, contract details, and billing information
- Binary target variable: Churn (Yes/No)

---

## 🔍 Key Findings

| Metric | Value | Insight |
|--------|-------|---------|
| **Overall Churn Rate** | ~32% | High - requires immediate attention |
| **Month-to-Month Churn** | ~75% | Contract type is #1 churn predictor |
| **Fiber Optic Churn** | ~50% | Potential service quality issues |
| **Electronic Check Churn** | ~60% | Payment method impacts retention |
| **New Customer Churn (0-12m)** | ~55% | Critical onboarding period |

### High-Risk Customer Profile
- Month-to-month contract
- Fiber optic internet
- Electronic check payment
- Tenure less than 12 months
- No add-on services (tech support, security)

---

## 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| **Language** | Python 3.8+ |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Statistical Analysis** | SciPy |
| **Database Queries** | SQL |
| **IDE** | Jupyter Notebook / VSCode |

---

## 📁 Project Structure

```
customer-churn-analysis/
│
├── 📂 data/
│   └── telecom_customers.csv       # Customer dataset
│
├── 📂 visualizations/              # Generated charts and graphs
│   ├── 01_churn_distribution.png
│   ├── 02_churn_by_contract.png
│   ├── 03_charges_distribution.png
│   ├── 04_tenure_boxplot.png
│   ├── 05_service_heatmap.png
│   ├── 06_payment_method_churn.png
│   └── 07_dashboard.png
│
├── 📄 customer_churn_analysis.py   # Main analysis script
├── 📄 sql_queries.sql              # SQL queries for analysis
├── 📄 requirements.txt             # Python dependencies
└── 📄 README.md                    # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-analysis.git
cd customer-churn-analysis

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the analysis
python customer_churn_analysis.py
```

---

## 📈 Analysis Components

### 1. Data Exploration
- Dataset structure and statistics
- Missing value detection
- Data type verification

### 2. Data Cleaning & Preprocessing
- Handling missing values
- Feature engineering (tenure categories, charge buckets)
- Data type conversions

### 3. Exploratory Data Analysis (EDA)
- Churn distribution analysis
- Demographic impact on churn
- Service feature correlation
- Tenure and revenue patterns

### 4. Statistical Analysis
- **T-Test**: Monthly charges comparison (churned vs retained)
- **Chi-Square Test**: Contract type vs churn relationship
- **Correlation Analysis**: Feature relationships with churn

### 5. Data Visualization
- Distribution plots
- Comparative bar charts
- Box plots for numerical features
- Heatmaps for service adoption
- Comprehensive dashboard

---

## 📊 Visualizations

### Churn Distribution
Pie chart and bar graph showing overall churn rate

### Contract Analysis
Comparison of churn rates across different contract types

### Revenue Analysis
Monthly charges distribution segmented by churn status

### Tenure Analysis
Box plot showing tenure patterns for churned vs retained customers

### Service Adoption Heatmap
Visual representation of service feature adoption rates

### Dashboard
Comprehensive view combining multiple key metrics

---

## 💡 Business Recommendations

### 1. Contract Strategy
- Incentivize long-term contracts with discounts
- Create loyalty milestone rewards
- Offer upgrade paths for month-to-month customers

### 2. Service Quality
- Investigate fiber optic service issues
- Implement proactive support for fiber customers
- Regular satisfaction surveys

### 3. Senior Citizen Program
- Dedicated support channels
- Simplified billing options
- Personalized assistance programs

### 4. Payment Optimization
- Incentivize auto-pay enrollment
- Offer discounts for stable payment methods
- Reduce friction in payment process

### 5. New Customer Retention
- 90-day onboarding program
- Proactive check-ins during first year
- Early warning system for at-risk customers

---

## 🗄 SQL Queries

The `sql_queries.sql` file contains production-ready queries for:

- Basic data exploration
- Churn rate by demographics
- Service feature analysis
- Tenure bucket analysis
- Revenue impact calculations
- Multi-factor risk segmentation
- Customer cohort analysis
- CLV estimation
- High-risk customer identification

---

## 🔮 Future Enhancements

- [1] **Machine Learning Model**: Build predictive churn model using scikit-learn
- [2] **Real-time Dashboard**: Interactive dashboard with Plotly/Dash
- [3] **A/B Testing Framework**: Measure retention campaign effectiveness
- [4] **Automated Reporting**: Scheduled analysis reports
- [5] **API Integration**: Connect with CRM systems

---

## 👤 Author

**[Your Name]**

- LinkedIn: [https://www.linkedin.com/in/vivek-reddy-solipeta-588729227?lipi=urn%3Ali%3Apage%3Amessaging_thread%3B753221cb-285f-4cca-81d6-8478a73521c6]
- Email: vivekreddysolipeta2003@gmail.com
- GitHub: [@vivekreddy2003](https://github.com/vivekreddy2003)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Dataset inspired by telecom industry customer behavior patterns
- Visualization techniques from Seaborn gallery
- Statistical methods from SciPy documentation

---

⭐ **If you found this project helpful, please give it a star!** ⭐

