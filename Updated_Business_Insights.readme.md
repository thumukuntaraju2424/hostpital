
# Data Preprocessing and Business Insights

This document outlines the critical steps involved in preparing data for analysis, visualization, and reporting. Proper preprocessing ensures **accuracy**, **consistency**, and **reliability** of insights.

---

## Data Preprocessing Steps

### 1. Data Inspection and Profiling
- Inspect dataset structure (rows, columns).
- Identify data types of each column.
- Detect missing values and duplicates.

### 2. Handling Missing Values
- Check critical fields: `current_stock`, `reorder_level`, `stock_value`, `days_to_expiry`.
- Impute missing values using mean/median, or flag anomalies for review.

### 3. Correcting Data Types
- Ensure numerical fields: `current_stock`, `reorder_level`, `stock_value`.
- Ensure date fields: `last_order_date`, `expiry_date`.

### 4. Handling Outliers
- Evaluate numerical columns (`stock_value`, `turnover_rate`) for unusual values.
- Use box plots or other visualization methods.
- Decide to remove, transform, or retain outliers depending on analysis goals.

### 5. Data Cleaning and Standardization
- Standardize identifiers (`vendor_id`, `sku_id`).
- Normalize categorical fields (e.g., `stock_status` should only include `Critical_Low`, `Low`, `Adequate`).

### 6. Feature Engineering
- Derive new metrics such as *risk categories* from `days_to_expiry`:
  - Example: `"High Risk"`, `"Low Risk"`.
- Create features that enhance interpretability for visualization and reporting.

### 7. Data Aggregation and Transformation
- Summarize values at higher levels (e.g., per `vendor_id` or `hospital_id`).
- Apply aggregation functions: **sum, mean, count**.
- Ensure raw data is transformed into stakeholder-friendly insights.

### 8. Final Validation
- Perform sanity checks:
  - Ensure `current_stock >= 0`.
  - Verify derived metrics.
- Validate formats, ranges, and data integrity.
- Confirm readiness of dataset for **Tableau / Power BI** visualization.

---


 
# 🏥  Business Insights


![Hospital Analytics Header](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/8a2dccc7-9f07-4c6c-9879-c2c269d04d8a.png)

---

## 📊 Overview

This analytics project leverages interactive Power BI dashboards to reveal actionable operational and financial insights for hospital leadership. By visualizing trends and patterns across departments and vendors, the report empowers decision-makers with robust data to improve care delivery, resource allocation, and cost management.

---

## 📌 Key Business Insights

### 🚑 Hospital Administrator Dashboard

#### **Patient Load by Department**  
- **Emergency Medicine** (16.7K patients) and **Cardiology** (12.2K) are the busiest departments, indicating critical staffing and resource priorities for these units.  
- Strategic hiring and automation focus here can prevent bottlenecks and improve throughput.

#### **Total Revenue and Cost Over Time**  
- Revenue and costs showed strong growth early in 2024, peaking at 0.6M, followed by a sharp drop to 0.25M in April, which warrants investigation for any operational or external causes.  
- Consider a financial review to understand seasonal effects or anomalies impacting income or expenses.

#### **Top 5 Vendors Performance**  
- Significant variation observed:  
  - **Western Medicals**: Highest quality rating (5.5/5), lowest delivery days late  
  - **Zoom Pharma**: Lowest quality (3/5), highest days late (31.55)  
- Optimize vendor contracts by prioritizing those with higher service levels and reliability.

#### **Average Length of Stay by Department**  
- **Internal Medicine** (5.7 days) and **Cardiology** (5.6 days) have the longest stays; **Emergency Medicine** is the shortest (1.5 days).  
- Departments with longer stays may benefit from workflow or discharge planning improvements.

---

### 👩‍🔬 Department Head Dashboard

#### **Budget vs Actual Spend**  
- The department operated well within budget (7.21M allocated, 3.6M spent), suggesting strong cost controls and opportunities for further targeted investments.

#### **SKUs Consumed by Transaction Type**  
- **Procedures** consume 46K units versus 27K for prescriptions. Focus procurement strategies on high-use procedural inventory to control costs.

#### **Revenue Lost by Category**  
- Main reasons for lost revenue:  
  - High Cost (6.86M)  
  - Insurance Issues (4.24M)  
  - Patient Declined (3.39M)  
- Actions should center on reducing costs, improving insurance claim processes, and enhancing patient engagement.

#### **Top 10 Consumed SKUs**  
- **XL Reagents**, surgical gloves, and drapes dominate usage, indicating a need for consolidating supplier contracts and negotiating bulk pricing.

---

## 📝 Additional Recommendations

- **Staff Optimization:** Redirect staffing to Emergency and Cardiology during peak times.
- **Vendor Management:** Review or renegotiate contracts with vendors showing high delays or low quality.
- **Cost Analysis:** Deep-dive revenue dips post-March to understand and mitigate root causes.
- **Inventory Planning:** Leverage SKU consumption data for high-volume purchasing agreements.

---

## 🧭 Conclusion

These dashboards demonstrate that targeted staffing, smart vendor management, improved discharge processes, and focused procurement are key actionable strategies for hospital performance improvement. Immediate attention to outlier cost/revenue trends, high-volume departments, and inventory consolidation will maximize both quality of care and operational efficiency. Leveraging visual analytics is essential for continuous improvement in a dynamic healthcare environment.

---


