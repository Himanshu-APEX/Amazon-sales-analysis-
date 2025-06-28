# Amazon-sales-analysis-


This project presents an end-to-end business intelligence solution, transforming raw Amazon sales transaction data into **cleaned, structured insights** using **Python (Pandas)** and visualized through a dynamic **Power BI dashboard**. The project aims to deliver actionable insights to support business strategy, customer understanding, and operational optimization.

---

## 🎯 Project Objective

To analyze Amazon's sales data and uncover patterns in **product performance**, **customer behavior**, **fulfillment efficiency**, and **regional sales trends** by combining **data preprocessing** in Python with **interactive dashboarding** in Power BI.

---

## 🧰 Tools & Technologies

| Tool                  | Purpose                                                 |
| --------------------- | ------------------------------------------------------- |
| **Excel**             | Initial data source (CSV format)                        |
| **Python**            | Data cleaning & feature engineering                     |
| → `pandas`            | Handling missing values, filtering, grouping, RFM logic |
| → `datetime`          | Date parsing and numeric operations                     |
| **Power BI**          | Data modeling, KPI tracking, visual storytelling        |

---

## 📦 Dataset Overview

* **File**: `amazon_sales_cleaned.csv`
* **Rows**: around 130,000 sales transactions
* **Key Fields**:

  * `Order ID`, `Date`, `Category`, `Qty`, `Amount`
  * `Fulfilment`, `Status`, `ship_city`, `ship_state`

---

## 🧹 Data Cleaning Highlights (Python)

* Converted `Date` column to datetime format
* Extracted **Quarter**, **Month**, and **Year** for time analysis
* Filled missing values for `Amount`, `Currency`, and `Shipping fields`
* Standardized status labels (e.g., shipped, returned, cancelled)
* Removed irrelevant or zero-variance columns
* Grouped delivery statuses into meaningful categories for better visuals

---

## 📊 Power BI Dashboard Features

* **KPI Cards**: Total Revenue, Total Orders, Avg. Order Value, Qty Sold
* **Trend Line Chart**: Monthly sales growth
* **Top Categories (Bar Chart)**: Products driving revenue (T-Shirts, Shirts)
* **Fulfillment Analysis (100% Stacked Bar)**: Delivered vs Cancelled
* **RFM Scatter Plot**: Customer segmentation
* **Top Cities Table**: Qty, Revenue, Avg Order Value (with Top N filter)
* **Slicers**: Date, Category, Fulfillment Type, Status

---

## 🔍 Key Insights

* **T-Shirts & Shirts** dominate sales by revenue
* **Q2** shows peak performance — indicating a seasonal trend
* **Amazon Fulfillment** outperforms merchant in delivery success
* **Customer behavior** segmented using RFM (Recency, Frequency, Monetary)
* **Major revenue concentration** in specific states and metro cities

---

## Repository Structure

* amazon_sales_cleaned.csv: Input dataset.
*  amazon.ipynb: Jupyter Notebook with data cleaning, analysis, and visualization code.
* Dashboard link .pbix
* outputs/: Directory with exported CSVs (e.g., daily_sales.csv, category_summary.csv) and charts (e.g., category_revenue.png).
* README.md: Project overview and instructions.

---

## ✅ Outcome

This analysis provides Amazon's sales team and stakeholders with the ability to:

* Monitor business KPIs in real time
* Identify underperforming categories or locations
* Improve fulfillment operations
* Drive retention with customer segmentation

---
Contact

For questions or contributions, contact Himanshu Kumar at [himanshuk3512@gmail.com] or open an issue on GitHub.

Thank you for exploring this project!
