# 🛍️ Zopper Device Insurance Attach Analysis  

This project analyzes **store-level device insurance attach percentage data** to identify performance patterns, operational gaps, and improvement opportunities across retail stores. The analysis also includes a **January attach percentage forecast** using recent performance trends.  

An optional **interactive Streamlit dashboard** is built to enable business users to explore insights easily.

The project follows an **industry-style analytics workflow** including data understanding, cleaning, analysis, segmentation, forecasting, and deployment.

---

## 🧠 Problem Statement  
Retail partners sell large volumes of devices, but insurance attach rates vary significantly across stores. Low attach rates directly impact revenue and customer protection coverage.

This project answers:

> **"How can store-level attach performance be analyzed, improved, and forecasted using historical data?"**

---

## 🔹 Dataset Columns

| Column Name | Description |
|------------|-------------|
| Branch | Regional branch name |
| Store_Name | Retail store identifier |
| Aug–Dec | Monthly insurance attach percentage |

---

## 🎯 Objectives

Build an analytical system that:

✅ Identifies month-wise attach trends  
✅ Compares branch and store-level performance  
✅ Highlights top and bottom performing stores  
✅ Categorizes stores for targeted interventions  
✅ Forecasts January attach percentages  
✅ Presents insights in a business-friendly manner  

---

## ⚙️ Tech Stack

| Layer | Technologies |
|------|-------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Analytics | Descriptive statistics |
| Forecasting | Weighted average method |
| Deployment | Streamlit |
| Notebooks | Jupyter |
| Version Control | Git, GitHub |

---

## 🔄 Analytics Workflow

### ✅ 1. Data Understanding  
Performed in `01_data_understanding.ipynb`

✔ Validated data structure  
✔ Checked completeness  
✔ Identified variability and zero-attach stores  
✔ Assessed overall attach distribution  

---

### ✅ 2. Data Cleaning & Reshaping  
Performed in `02_data_cleaning.ipynb`

✔ Converted wide data to long format  
✔ Ensured numeric consistency  
✔ Standardized month ordering  
✔ Created analysis-ready dataset  

---

### ✅ 3. Month, Branch & Store Analysis  
Performed in `03_month_branch_store_analysis.ipynb`

Key insights:
- Attach rates improve toward year end  
- High variability exists across stores  
- Store-level execution impacts performance more than region  
- Clear top and bottom performers identified  

---

### ✅ 4. Store Categorization  
Performed in `04_store_categorization.ipynb`

Stores were classified into:
- High Performers  
- Medium Performers  
- Low Performers  
- Inactive Stores  

This enables **targeted business action**.

---

### ✅ 5. January Attach % Forecast  
Performed in `05_january_prediction.ipynb`

Forecasting logic:

January Attach % = 0.5 × December + 0.3 × November + 0.2 × October

---

## 🌐 Streamlit Dashboard  

An interactive dashboard built using **Streamlit** to visualize:

### Features:
✅ Overall attach snapshot  
✅ Month-wise trend  
✅ Branch and store performance  
✅ Store-level January predictions  
✅ Branch-based filtering  

---

## 📌 Key Business Insights

- Attach performance improves during peak sales periods  
- A small number of stores consistently outperform others  
- Several stores remain inactive across months  
- Store-level execution drives results more than geography  
- Targeted interventions can significantly improve attach rates  

---

## 💡 Business Recommendations

- Replicate best practices from high-performing stores  
- Focus training and incentives on low and inactive stores  
- Monitor volatile stores to stabilize performance  
- Use January forecasts for planning targets and incentives  

---

## 👨‍💻 Author  
**Girish K S**  

Data Scientists

Email: girishhemanth823@gmail.com
