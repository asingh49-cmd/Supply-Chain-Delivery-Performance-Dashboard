# Supply-Chain-Delivery-Performance-Dashboard

> Analyzing 180,000+ global supply chain orders to identify delivery bottlenecks, predict late delivery risk, and optimize logistics operations.

[![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?logo=tableau)](https://public.tableau.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)

---

## 📊 Project Overview

This project analyzes global supply chain delivery performance using the DataCo Supply Chain dataset from Kaggle. The analysis identifies operational inefficiencies, predicts late delivery risks using machine learning, and provides actionable insights through interactive Tableau dashboards.

### Business Problem
Supply chain delivery performance directly impacts customer satisfaction and operational costs. With an industry benchmark of 95% on-time delivery (OTD), this project aims to:
- Identify factors causing delivery delays
- Predict which orders are at risk of late delivery
- Provide recommendations to improve OTD rate
- Optimize shipping mode allocation and routing

---

## 🎯 Project Goals

- **Analyze** delivery performance across markets, shipping modes, and customer segments
- **Identify** root causes of late deliveries and high-risk patterns
- **Build** a predictive model to flag at-risk orders before they're late
- **Create** interactive dashboards for operational decision-making
- **Recommend** data-driven improvements to supply chain operations

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python 3.8+** | Data cleaning, feature engineering, machine learning |
| **MySQL** | Database management, SQL query practice |
| **Tableau Public** | Interactive dashboards and visualizations |
| **pandas & numpy** | Data manipulation and analysis |
| **scikit-learn** | Predictive modeling (Random Forest) |
| **Jupyter Notebook** | Documentation and analysis workflow |

---

## 📁 Project Structure
```
supply_chain_project/
├── data/
│   ├── raw/                          # Original dataset (not committed)
│   │   └── DataCo_Supply_Chain.csv
│   └── processed/                    # Cleaned data for analysis
│       ├── supply_chain_cleaned.csv
│       └── model_predictions.csv
│
├── scripts/
│   ├── 01_data_cleaning.py          # Data cleaning & feature engineering
│   ├── 02_load_to_mysql.py          # Load data to MySQL database
│   └── 03_predictive_model.py       # Machine learning model
│
├── sql/
│   ├── create_tables.sql            # Database schema
│   └── analytical_queries.sql       # Business intelligence queries
│
├── images/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Source:** [DataCo Global Supply Chain Dataset](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) (Kaggle)

**Size:** 180,000+ orders

**Features:** 53 columns including:
- Order information (date, status, ID)
- Shipping details (mode, origin, destination, delivery time)
- Customer data (segment, location)
- Product information (category, price, quantity)
- Delivery metrics (scheduled vs actual days, late delivery risk)
- Financial data (sales, profit, discounts)

**Geographic Coverage:** 5 global markets (North America, Latin America, Europe, Asia-Pacific, Africa)

---

## 🔑 Key Metrics & KPIs

### Primary Metrics
- **On-Time Delivery Rate (OTD):** % of orders delivered by scheduled date
- **Average Delivery Time:** Mean days from order to delivery
- **Perfect Order Rate:** % of orders delivered on-time, complete, and fraud-free
- **Late Delivery Risk Score:** Probability of order arriving late

### Secondary Metrics
- Delivery time variance by shipping mode
- Geographic performance (OTD by market/country/state)
- Customer segment analysis
- Shipping cost efficiency
- Delay distribution and patterns

---

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# MySQL 8.0 or higher
mysql --version
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/asingh49-cmd/Supply-Chain-Delivery-Performance-Dashboard.git
cd supply-chain-analysis
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the dataset**
- Go to [Kaggle DataCo Supply Chain Dataset](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
- Download `DataCoSupplyChainDataset.csv`
- Place in `data/raw/` folder

4. **Set up MySQL database**
```bash
mysql -u root -p
CREATE DATABASE supply_chain_db;
```

5. **Run data pipeline**
```bash
# Clean and process data
python scripts/01_data_cleaning.py

# Load to MySQL
python scripts/02_load_to_mysql.py

# Build predictive model
python scripts/03_predictive_model.py
```

---

## 📈 Analysis Plan

### Phase 1: Data Preparation ✅
- [x] Download dataset
- [ ] Data cleaning and validation
- [ ] Feature engineering
- [ ] Load to MySQL database

### Phase 2: Exploratory Analysis ⏳
- [ ] Calculate key KPIs
- [ ] Identify trends and patterns
- [ ] Geographic performance analysis
- [ ] Shipping mode comparison

### Phase 3: Predictive Modeling ⏳
- [ ] Build late delivery risk model
- [ ] Feature importance analysis
- [ ] Model evaluation and validation
- [ ] Generate predictions for Tableau

### Phase 4: Dashboard Development ⏳
- [ ] Executive Summary dashboard
- [ ] Operational Deep Dive dashboard
- [ ] Geographic Analysis dashboard
- [ ] Risk Analytics dashboard

### Phase 5: Documentation & Deployment ⏳
- [ ] Publish to Tableau Public
- [ ] Document findings and insights
- [ ] Create presentation materials
- [ ] Portfolio integration

---

## 🎨 Dashboards (Coming Soon)

### 1. Executive Summary
High-level KPIs and trends for leadership decision-making

### 2. Operational Deep Dive
Detailed performance metrics by shipping mode, market, and time period

### 3. Geographic Analysis
Interactive maps showing regional performance and problem areas

### 4. Risk Analytics
Predictive insights on at-risk orders and delay factors

**Live Dashboards:** [Link to be added after publication]

---

## 🔍 Expected Insights

Based on initial data exploration, the analysis will investigate:
- Why certain shipping modes underperform despite similar delivery times
- Which geographic markets have the lowest OTD rates
- Whether order value correlates with delivery performance
- What factors most strongly predict late deliveries
- How customer segments differ in delivery experience
- Seasonal patterns and their impact on performance

---

## 📊 SQL Queries

Sample analytical queries available in `sql/analytical_queries.sql`:
- Overall performance metrics
- Shipping mode comparison
- Geographic performance rankings
- Late delivery root cause analysis
- Customer segment analysis
- Time-based trend analysis

---

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Classifier

**Target Variable:** Late Delivery Risk (binary classification)

**Features:**
- Scheduled delivery days
- Order quantity and value
- Shipping mode
- Customer segment
- Market/geographic region
- Temporal features (month, day of week)

**Evaluation Metrics:**
- Accuracy
- Precision/Recall
- ROC-AUC Score
- Feature Importance

---

## 📝 Key Findings

> *This section will be updated as analysis progresses*

### Current Status
- Dataset loaded: 180,520 orders
- Date range: [To be determined]
- Markets: 5 global regions
- Shipping modes: 4 types

### Preliminary Observations
- [To be added after EDA]

---

## 💡 Recommendations

> *Business recommendations will be added after completing analysis*

---

## 🗂️ Requirements
```txt
pandas>=1.5.0
numpy>=1.23.0
mysql-connector-python>=8.0.0
pymysql>=1.0.0
sqlalchemy>=2.0.0
scikit-learn>=1.2.0
jupyter>=1.0.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Dataset provided by DataCo on Kaggle
- Inspired by real-world supply chain analytics challenges

---

**Last Updated:** December 28, 2024
