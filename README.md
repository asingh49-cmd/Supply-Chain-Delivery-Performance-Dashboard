# Supply-Chain-Delivery-Performance-Dashboard

> End-to-end analytics project Analyzing 180,000+ global supply chain orders to identify delivery bottlenecks, predict late delivery risk, and optimize logistics operations.

[![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?logo=tableau)](https://public.tableau.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)

**Link to Dashboard:** [Dashboard](https://public.tableau.com/views/SupplyChainPerformanceDashboard_17674118692570/ExecSummaryKPIs?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
---

## Project Overview

This project analyzes global supply chain delivery performance using the DataCo Supply Chain dataset from Kaggle. The analysis identifies operational inefficiencies, predicts late delivery risks using machine learning, and provides actionable insights through interactive Tableau dashboards.

### Business Problem
Supply chain delivery performance directly impacts customer satisfaction and operational costs. With an industry benchmark of 95% on-time delivery (OTD), this project aims to:
- Identify factors causing delivery delays
- Predict which orders are at risk of late delivery
- Provide recommendations to improve OTD rate
- Optimize shipping mode allocation and routing

---

## Tools & Technologies

### Data Processing & Analysis
- **Python 3.12**: Data cleaning, feature engineering, machine learning
  - `pandas` & `numpy`: Data manipulation
  - `scikit-learn`: Predictive modeling (Random Forest, Logistic Regression)
  - `matplotlib` & `seaborn`: Exploratory visualizations
  - `easyNMT`: Data Translation (Countries and State were originally in Spanish)
  - `sqlalchemy` & `pymysql`: Database connection and test queries

### Database & Queries
- **MySQL 8.0**: Data warehousing and SQL analysis
  - Analytical queries for root cause investigation
  - Created views and aggregations for dashboard consumption

### Visualization & Dashboards
- **Tableau Public**: Interactive dashboards
  - 3 comprehensive dashboards with 15+ visualizations
  - Global filters for dynamic exploration
  - Published to Tableau Public for portfolio showcase

### Development Tools
- **Git/GitHub**: Version control
- **VS Code**: Development environment

---

## Project Structure
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
│   └── analytical_queries.sql       # Business intelligence queries
│
├── images/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Dataset

**Source:** [DataCo Supply Chain Dataset](https://www.kaggle.com/datasets/evilspirit05/datasupplychain?resource=download) (Kaggle)

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

## Approach

1. **Data Cleaning & Feature Engineering (Python)**
- 80+ engineered features including temporal patterns, customer behavior, geographic complexity
- Handled missing values and outliers
- Created target variable based on scheduled vs. actual delivery times

2. **Exploratory Analysis (SQL + Tableau)**
- 10+ analytical SQL queries investigating root causes
- Geographic, temporal, and operational pattern analysis
- Customer segment and product category performance

3. **Predictive Modeling (Python - scikit-learn)**
- Compared Logistic Regression vs Random Forest
- Selected Random Forest for 21.6% better recall (catches more late deliveries)
- Model trained on 80% data, validated on 20% test set

4. **Interactive Dashboards (Tableau Public)**
- Executive Summary KPI overview
- Operational Deep Dive for root cause analysis
- Predictive Analytics for model performance and high-risk order monitoring

---

## Getting Started

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
python scripts/data_cleaning.py

# Load to MySQL
python scripts/load_to_mysql.py

# Build predictive model
python scripts/predictive_model.py
```

6. **Run SQL Queries**

```bash
# Execute SQL queries
mysql -u root -p supply_chain_db < sql/analytical_queries.sql
```

---
## SQL Analysis Summary

- **Systemic Underperformance:** On-time delivery (OTD) averages ~42–43% across all markets, months, and segments, indicating a structural operational issue rather than seasonal or regional variability.
- **Payment Method Effect:** Transfer payments consistently outperform other methods by 7–10 percentage points in OTD across every market, suggesting workflow best practices that can be replicated.
- **Shipping Mode Misalignment:** First Class shipping shows a 0% OTD rate despite premium pricing, while Standard Class (lowest cost) achieves the highest OTD (~60%), highlighting a critical service-level and pricing mismatch.
- **Staffing Not a Factor:** Weekend and weekday OTD rates are nearly identical, ruling out weekend staffing or capacity constraints as primary causes.

---

## Dashboards

### 1. Executive Summary
High-level KPIs and trends for leadership decision-making

### 2. Operational Deep Dive
Detailed performance metrics by shipping mode, market, and time period

### 3. Predictive Analytics
Predictive insights on high-risk orders and model performance

---

## Machine Learning Model

### Model Selection: Random Forest
**Decision Criteria**: Prioritized **Recall** over accuracy to maximize late delivery detection
**Business Justification**: Missing a late delivery (False Negative) creates customer dissatisfaction, while a false alarm (False Positive) only creates minor operational overhead. Therefore, maximizing Recall is more valuable than minimizing False Positives.

**Target Variable:** Late Delivery Risk (binary classification)

**Features:**
- Sales 
- Order Discount
- Order Profit
- Order quantity (bulk or not)
- Product Category
- Transaction type
- Market/geographic region
- Temporal features (year, quarter, weekend/weekday)

**Evaluation Metrics:**
- Accuracy
- Precision/Recall
- ROC-AUC Score
- Feature Importance

---

## Key Findings - Dashboard Analysis

### Dashboard 1: Executive Summary (KPI Overview)

**Purpose**: High-level performance metrics for leadership decision-making

**Key Visualizations**:
- **KPI Cards**: Total orders (180,519), OTD rate (42.7%), avg delivery days (3.5), late delivery risk (50.1%)
- **Monthly OTD Trend**: Flat performance at 42-43% with industry standard reference line at 95%
- **Shipping Mode Performance**: Bar chart showing average delivery days by mode
- **Geographic Heat Map**: World map showing OTD rates by country (predominantly red/orange indicating poor performance)

**Critical Insights**:
- **52.3 percentage point gap** between actual (42.7%) and target (95%) OTD
- **No improvement trend** over 48 months - indicates structural problems
- **Global underperformance** - all markets and shipping modes affected
- **Revenue at risk** from customer dissatisfaction across 103,400 late orders

**Annotation**: "Consistently poor performance - no seasonal pattern suggests structural operational issues"

### Dashboard 2: Operational Deep Dive

**Purpose**: Detailed root cause analysis for operations managers

**Key Visualizations**:

1. **Late Delivery Root Causes (Treemap)**
   - Market × Shipping Mode × Product Category hierarchy
   - LATAM + Standard Class = largest contributor to late deliveries
   - Color-coded by shipping mode for pattern identification

2. **Days for Shipping vs Frequency (Histogram)**
   - Peak at 1-2 days (58K orders) - mostly on-time (orange)
   - Orders taking 3-7 days predominantly late (blue)
   - **Critical finding**: 2-day threshold is inflection point where operations break down

3. **Shipping Mode × Market Matrix (Heat Map)**
   - Shows late delivery rate by combination
   - **First Class: 100% late rate** across all markets (dark red) - systematic failure
   - **Same Day: ~47% late rate** (green) - relatively better but still unacceptable
   - **Standard Class: 40% late rate** (green) - outperforms premium services

4. **Customer Segment Analysis (Stacked Bar)**
   - Consumer: 95K orders, ~43% OTD
   - Corporate: 55K orders, ~47% OTD
   - Home Office: 30K orders, ~38% OTD
   - All segments affected; no preferential treatment observed

**Critical Insights**:
- **First Class dysfunction**: 100% late rate despite premium pricing - immediate audit required
- **Standard Class paradox**: Cheapest option outperforms expensive options
- **Transfer payment advantage**: 44% vs. 52% late rate - workflow investigation opportunity
- **Volume concentration**: 60K orders at 1-2 day window - optimization leverage point

**Filters**: Market, Shipping Mode, On-Time Status, Order Year slider


### Dashboard 3: Predictive Analytics

**Purpose**: ML model performance monitoring and high-risk order identification

**Important**: This dashboard analyzes **test set only (36,104 orders = 20% of data)**. Model trained on remaining 80%.

**Key Visualizations**:

1. **Model Performance KPIs**
   - Accuracy: 55.4%
   - Precision: 57.3%
   - Recall: 73.4% (catches ~3 out of 4 late deliveries)
   - F1-Score: 64.3%

2. **Confusion Matrix**
```
   Predicted:        0 (On-time)  |  1 (Late)
   ───────────────────────────────┼──────────────
   Actual 0:         5,464 (TN)   |  10,844 (FP)
   Actual 1:         5,268 (FN)   |  14,528 (TP)
```
   - **True Positives: 14,528** - Correctly predicted late orders (actionable)
   - **False Negatives: 5,268** - Missed late orders (improvement opportunity)
   - **False Positives: 10,844** - False alarms (acceptable operational overhead)

3. **Risk Score Distribution**
   - Histogram showing concentration at 50-55% probability
   - Bimodal distribution indicates model uncertainty
   - Few orders in extreme risk categories (<30% or >70%)

4. **Late Delivery Probability by Market & Payment Type (Matrix)**
   - CASH/DEBIT/PAYMENT: 51-53% late probability
   - TRANSFER: 42-45% late probability (consistently better)
   - Minimal market variation; payment type is stronger predictor

5. **High-Risk Orders Table**
   - Drillable detail table showing individual order characteristics
   - Filterable by risk category, market, customer segment
   - Enables proactive intervention on at-risk orders

**Business Impact**:
- **14,528 late deliveries identified** in advance (73.4% catch rate)
- **5,268 late deliveries missed** (26.6%) - room for model improvement
- **10,844 false alarms** - operational overhead but justified by catch rate
- **Random Forest selected** for 21.6% better recall vs Logistic Regression (catches 4,277 more late orders)

**Model Limitations**:
- 55% accuracy indicates high inherent randomness in late deliveries
- Limited to order characteristics; lacks real-time operational data
- Class imbalance (57% late) creates challenging prediction environment

**Filters**: Risk Probability slider, Risk Category (High/Medium/Low), Customer Segment, Order Year slider

---

### Model Limitations & Why Accuracy is Modest (55%)

**Root Causes of 55% Accuracy**:

1. **High Inherent Randomness**
   - Late deliveries driven by unpredictable factors: traffic, weather, staffing, carrier issues
   - Many variables outside the data's scope

2. **Limited Features Available**
   - No real-time traffic conditions
   - No weather data
   - No carrier-specific performance metrics
   - No warehouse capacity indicators
   - No real-time inventory status
   - Only used pre-delivery order characteristics (no "future leak")

3. **Class Imbalance**
   - 57% of orders late creates challenging prediction environment
   - Model tends toward predicting "late" more frequently

4. **Data Leakage Prevention**
   - Deliberately excluded `days_for_shipping_real`, `actual_delivery_days`, `delay_days` (only known after delivery)
   - Ensures model uses only information available at order time

---

## Next Steps & Enhancements

- **Enrich Model Inputs:** Integrate external data sources such as weather (NOAA), traffic congestion, and warehouse/inventory capacity metrics to improve prediction accuracy.
- **Data Quality Improvements:** Evaluate and incorporate more reliable or higher-granularity operational data sources to reduce noise and bias in model inputs. Potentially use another data source for performance data.
- **Advanced Analytics:** Extend the current model with time-series forecasting to anticipate risk trends and capacity bottlenecks.
- **Automated Interventions:** Design a rules-based or ML-driven alerting system to proactively trigger operational actions for high-risk orders.
- **What-If Analysis:** Develop a predictive scenario dashboard allowing stakeholders to simulate changes in shipping mode, market, or order characteristics and observe risk impacts in real time.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- Dataset provided by DataCo on Kaggle
- Inspired by real-world supply chain analytics challenges

---

**Last Updated:** January 4th, 2026