# 🏬 Retail Store Performance Comparator

An interactive Streamlit analytics dashboard that compares the performance of retail stores across key business KPIs such as **Sales**, **Profit**, and **Transactions**.

The dashboard enables business users to quickly identify top-performing stores, analyze monthly trends, and uncover performance gaps through interactive filters and visual comparisons.

---

# 🚀 Project Overview

Retail organizations often operate multiple stores and need visibility into performance across locations.

This project demonstrates how **Python**, **Streamlit**, and **data visualization** can be combined to create an interactive decision-support dashboard that helps users:

* Compare two stores across selected KPIs
* Analyze monthly performance trends
* Generate quick executive insights
* Identify leading stores and performance gaps

The dashboard is designed for retail managers, analysts, and business stakeholders who need a simple way to evaluate store performance.

---

# 📊 Dashboard Preview

> Add dashboard screenshot here

```text
dashboard.png
```

The dashboard includes:

* KPI summary comparison
* Monthly performance visualization
* Automatic winner insight generation
* Dynamic filtering options

---

# 🧠 Key Features

## 🎛️ Interactive Filters

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

## 📈 KPI Summary

The dashboard automatically calculates and displays:

* Total KPI value for Store 1
* Total KPI value for Store 2

This provides an instant comparison of store performance.

---

## 💡 Executive Insight Generation

The application automatically generates business insights such as:

* 🏆 Winning store
* 📈 KPI lead difference
* 🤝 Equality detection when stores perform similarly

This simulates basic business insight generation and highlights key performance outcomes.

---

## 📊 Monthly Performance Visualization

A comparative bar chart displays:

* Monthly KPI values for Store 1
* Monthly KPI values for Store 2

This helps identify:

* Performance trends
* Seasonal variations
* Store-level strengths and weaknesses

---

# ⚙️ Technology Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming                |
| Streamlit  | Interactive dashboard framework |
| Pandas     | Data processing and analysis    |
| NumPy      | Numerical operations            |
| Matplotlib | Data visualization              |

---

# 📂 Project Structure

```text
retail-store-performance-comparator/
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

* Loads retail data
* Provides interactive filters
* Calculates KPIs
* Generates insights
* Visualizes monthly comparisons

---

## retail_data.csv

Sample retail dataset containing:

* Store Name
* Year
* Month
* Sales
* Profit
* Transactions

---

## dashboard.png

Screenshot preview of the dashboard.

---

## requirements.txt

Python dependencies required to run the project.

```bash
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

Open in your browser:

```text
http://localhost:8501
```

---

# 💼 Business Use Cases

This dashboard approach can be applied to:

* Retail chain performance monitoring
* Multi-store KPI comparison
* Sales performance analysis
* Store benchmarking
* Operational decision support

### Applicable Industries

* Retail chains
* E-commerce businesses
* Franchise networks
* Sales operations teams

---

# 🎯 Learning Outcomes

Through this project, I explored:

* Building interactive dashboards with Streamlit
* Data analysis using Pandas
* KPI comparison logic
* Business-focused visual storytelling
* Automated insight generation
* Interactive analytics application development

---

# 🔮 Future Enhancements

Potential improvements include:

* Compare multiple stores simultaneously
* Connect to SQL databases instead of CSV files
* Add predictive sales forecasting
* Include inventory and margin KPIs
* Deploy to Streamlit Cloud
* Add automated anomaly detection

---

# 👩‍💻 Author

**Rachel Purnima Johnpeter**

Data Analytics Lead transitioning into AI, Data Engineering, and Generative AI.

### Areas of Interest

* Data Analytics
* Machine Learning
* Generative AI
* AI-Powered Dashboards
* Decision Intelligence Systems

---

# 📌 Note

This project was built as part of my hands-on learning journey in **Python**, **Data Analytics**, and **Streamlit application development**.

It focuses on interactive KPI analysis, business insights, and dashboard-driven decision support for retail operations.
