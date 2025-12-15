import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Zopper Attach Analysis", layout="wide")

st.title("Zopper Device Insurance Attach Analysis")

# Load data
df_long = pd.read_csv("data/processed/zopper_attach_processed.csv")
jan_pred = pd.read_csv("outputs/january_attach_prediction.csv")

# KPI Section
st.subheader("Overall Snapshot")
col1, col2, col3 = st.columns(3)

col1.metric("Total Stores", df_long["Store_Name"].nunique())
col2.metric("Avg Attach %", round(df_long["Attach_Percentage"].mean()*100, 1))
col3.metric("Months Covered", df_long["Month"].nunique())

# Month-wise Trend
st.subheader("Month-wise Attach Trend")

month_avg = df_long.groupby("Month")["Attach_Percentage"].mean().reset_index()

fig, ax = plt.subplots()
ax.plot(month_avg["Month"], month_avg["Attach_Percentage"])
ax.set_ylabel("Attach %")
ax.set_xlabel("Month")
st.pyplot(fig)

# Branch Filter
st.subheader("January Attach % Prediction")

branches = jan_pred["Branch"].unique()
selected_branch = st.selectbox("Select Branch", branches)

filtered = jan_pred[jan_pred["Branch"] == selected_branch]
st.dataframe(filtered.sort_values("Jan_Predicted_Attach", ascending=False))
