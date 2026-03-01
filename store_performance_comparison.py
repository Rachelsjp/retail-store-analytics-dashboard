import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Retail Store Performance Comparator",
    layout="wide"
)

st.title("🏬 Retail Store Performance Comparator")
st.markdown("Compare retail stores across KPIs with monthly insights.")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("retail_data.csv")

df = load_data()

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("🔎 Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

month_order = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

available_months = [m for m in month_order if m in df["Month"].unique()]

selected_months = st.sidebar.multiselect(
    "Select Month(s)",
    available_months,
    default=available_months[:3]
)

stores = sorted(df["Store"].unique())

store1 = st.sidebar.selectbox("Select Store 1", stores, index=0)
store2 = st.sidebar.selectbox("Select Store 2", stores, index=1)

kpi_options = ["Sales", "Profit", "Transactions"]
selected_kpi = st.sidebar.selectbox("Select KPI", kpi_options)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------
filtered_df = df[
    (df["Year"] == selected_year) &
    (df["Month"].isin(selected_months))
]

store1_data = filtered_df[filtered_df["Store"] == store1]
store2_data = filtered_df[filtered_df["Store"] == store2]

store1_total = store1_data[selected_kpi].sum()
store2_total = store2_data[selected_kpi].sum()

# ---------------------------------------------------
# MAIN LAYOUT (LEFT + RIGHT)
# ---------------------------------------------------
left_col, right_col = st.columns([1.3, 1])

# ---------------------------------------------------
# LEFT COLUMN (KPI + EXECUTIVE INSIGHT)
# ---------------------------------------------------
with left_col:
    st.subheader("📊 KPI Summary")

    st.metric(f"{store1} {selected_kpi}", f"{store1_total:,}")
    st.metric(f"{store2} {selected_kpi}", f"{store2_total:,}")

    st.markdown("### 📌 Insight")

    difference = store2_total - store1_total

    if difference > 0:
        winner = store2
        lead = difference
    elif difference < 0:
        winner = store1
        lead = abs(difference)
    else:
        winner = None

    if winner:
        st.success(f"🏆 Winner: {winner}")
        st.write(f"📈 Lead: +{lead:,} {selected_kpi}")
    else:
        st.info("Both stores are performing equally.")

# ---------------------------------------------------
# RIGHT COLUMN (BAR CHART)
# ---------------------------------------------------
with right_col:
    st.subheader("📈 Monthly Comparison")

    # Ensure month order
    store1_data = store1_data.set_index("Month").reindex(selected_months).reset_index()
    store2_data = store2_data.set_index("Month").reindex(selected_months).reset_index()

    months = selected_months
    x = np.arange(len(months))
    width = 0.35

    fig, ax = plt.subplots(figsize=(6, 3))  # Balanced medium-small chart

    ax.bar(x - width/2, store1_data[selected_kpi], width, label=store1)
    ax.bar(x + width/2, store2_data[selected_kpi], width, label=store2)

    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.set_ylabel(selected_kpi)
    ax.legend(fontsize=8)

    plt.tight_layout()

    st.pyplot(fig)