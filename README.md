# 🏬 Retail Performance Analytics Dashboard

An interactive Streamlit analytics dashboard that compares the performance of retail stores across key business KPIs such as Sales, Profit, and Transactions.

The dashboard enables business users to quickly identify top-performing stores, monthly trends, and performance gaps using simple filters and visual comparisons.

---

# 🚀 Project Overview

Retail organizations often operate multiple stores and need to monitor performance across locations.

This project demonstrates how Python, Streamlit, and data visualization can be used to build an interactive decision-support dashboard that allows users to:

* Compare two stores across selected KPIs
* Analyze monthly performance trends
* Generate quick executive insights
* Identify leading stores and performance gaps

The dashboard is designed for retail managers and analysts to quickly evaluate store performance.

---

# 📊 Dashboard Preview

**dashboard.png**

This interactive dashboard includes:

* KPI summary comparison
* Monthly performance chart
* Automatic winner insight
* Dynamic filtering options

---

# 🧠 Key Features

## Interactive Filters

Users can dynamically filter the dashboard using:

* Year selection
* Month selection (multiple months)
* Store comparison (Store 1 vs Store 2)
* KPI selection

### Available KPIs

* Sales
* Profit
* Transactions

---

## KPI Summary

The dashboard automatically calculates and displays:

* Total KPI value for Store 1
* Total KPI value for Store 2

This allows quick comparison of store performance.

---

## Executive Insight Generation

The application automatically generates insights such as:

* 🏆 Winning store
* 📈 KPI lead difference
* Equality detection if both stores perform similarly

This simulates basic AI-style business insight generation.

---

## Monthly Performance Visualization

The dashboard provides a bar chart comparison showing:

* Store 1 monthly KPI values
* Store 2 monthly KPI values

This helps identify monthly trends and performance patterns.

---

# ⚙️ Technology Stack

| Tool       | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming                |
| Streamlit  | Interactive dashboard framework |
| Pandas     | Data processing                 |
| NumPy      | Numerical operations            |
| Matplotlib | Data visualization              |

---

# 📂 Project Structure

```text
retail-performance-analytics-dashboard
│
├── store_performance_comparison.py
├── retail_data.csv
├── dashboard.png
├── requirements.txt
└── README.md
```

---

# 📁 File Descriptions

## store_performance_comparison.py

Main Streamlit application that:

* Loads retail dataset
* Provides interactive filters
* Performs KPI calculations
* Generates insights
* Visualizes monthly store comparison

---

## retail_data.csv

Sample retail dataset containing:

* Store name
* Year
* Month
* Sales
* Profit
* Transactions

---

## dashboard.png

Screenshot preview of the interactive dashboard.

---

## requirements.txt

Python dependencies required to run the project.

```text
streamlit
pandas
matplotlib
numpy
```

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rachelsjp/retail-store-performance-comparator.git
```

## 2️⃣ Navigate to the Project Folder

```bash
cd retail-store-performance-comparator
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Streamlit Application

```bash
streamlit run store_performance_comparison.py
```

The dashboard will open in your browser:

```text
http://localhost:8501
```

---

# 💡 Business Use Cases

This dashboard approach can be used for:

* Retail chain performance monitoring
* Multi-store KPI comparison
* Sales performance analysis
* Store benchmarking
* Operational decision support

### Industries where similar dashboards are used

* Retail chains
* E-commerce companies
* Franchise businesses
* Sales operations teams

---

# 🎯 Learning Outcomes

Through this project I explored:

* Building interactive dashboards with Streamlit
* Data analysis using Pandas
* Data visualization using Matplotlib
* KPI comparison logic
* Automated business insight generation

---

# 🔮 Future Improvements

Possible future enhancements:

* Add multiple store comparison
* Integrate SQL database instead of CSV
* Add predictive sales forecasting
* Include additional KPIs (inventory, margins)
* Deploy dashboard to Streamlit Cloud

---

# 👩‍💻 Author

**Rachel Purnima Johnpeter**

Data Analytics Lead transitioning into AI / Data / Generative AI Engineering

### Areas of Interest

* Data Analytics
* Machine Learning
* Generative AI
* AI-powered dashboards
* Decision intelligence systems

---

# 📌 Note

This project was built as part of hands-on learning Python and Streamlit.

It focuses on interactive KPI analysis, business insights, and dashboard-driven decision support for retail operations.
