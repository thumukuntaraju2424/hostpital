import pandas as pd
import numpy as np

# ---  Load the datasets ---
transactions_df = pd.read_csv('Transaction_dataset.xlsx - Sheet1.csv')
patients_df = pd.read_csv('Updated_Enhanced_Patients_20250909_.xlsx - Sheet1.csv')
purchase_orders_df = pd.read_csv('Updated_Enhanced_Supply_Chain_20250909.xlsx - Purchase_Orders.csv')
deliveries_df = pd.read_csv('Updated_Enhanced_Supply_Chain_20250909.xlsx - Deliveries.csv')
inventory_df = pd.read_csv('Updated_Enhanced_Inventory_20250909_.xlsx - Sheet1.csv')
departments_df = pd.read_csv('Updated_Hospital_Dataset_20250909_193847.xlsx - Departments.csv')
physicians_df = pd.read_csv('Updated_Hospital_Dataset_20250909_193847.xlsx - Physicians.csv')
skus_df = pd.read_csv('Updated_Hospital_Dataset_20250909_193847.xlsx - SKUs.csv')
vendors_df = pd.read_csv('Updated_Hospital_Dataset_20250909_193847.xlsx - Vendors.csv')



# 1. Inventory Stock Status - Count of items for each stock_status
print(" Inventory Stock Status: ")
stock_status_distribution = inventory_df['stock_status'].value_counts()
print("\nDistribution of Inventory Stock Status:")
print(stock_status_distribution)
print("-" * 50)

# 2. Patient Demographics - Distribution of age_group and patient_type
print("  Patient Demographics: ")
patient_age_distribution = patients_df['age_group'].value_counts()
patient_type_distribution = patients_df['patient_type'].value_counts()
print("\nDistribution of Patient Age Groups:")
print(patient_age_distribution)
print("\nDistribution of Patient Types:")
print(patient_type_distribution)
print("-" * 50)


# 3. Supply Chain Urgency - Distribution of urgency_level in purchase orders
print(" Supply Chain Urgency: ")
po_urgency_distribution = purchase_orders_df['urgency_level'].value_counts()
print("\nDistribution of Urgency Levels in Purchase Orders:")
print(po_urgency_distribution)
print("-" * 50)


# 4. Transaction Cost Analysis - Total and average cost by transaction type
print(" Transaction Cost Analysis: ")
transaction_cost_analysis = transactions_df.groupby('transaction_type')['total_cost'].agg(['sum', 'mean']).sort_values(by='sum', ascending=False)
print("\nTotal and Average Cost by Transaction Type:")
print(transaction_cost_analysis)
print("-" * 50)


# 5. Bounced Transaction Analysis - Total revenue lost and common bounce reasons
print(" Bounced Transaction Analysis: ")
bounced_transactions = transactions_df[transactions_df['bounced'] == True]
total_revenue_lost = bounced_transactions['revenue_lost'].sum()
bounce_reason_counts = bounced_transactions['bounce_reason'].value_counts()
print(f"\nTotal Revenue Lost from Bounced Transactions: ${total_revenue_lost:,.2f}")
print("\nMost Common Bounce Reasons:")
print(bounce_reason_counts)
print("-" * 50)



# 6.  Patient Financials by Demographics (Insurance and Age)
print(" Patient Financials by Demographics:")
patient_transactions = pd.merge(transactions_df, patients_df, on='patient_id', how='left')
financial_by_demographics = patient_transactions.groupby(['insurance_type', 'age_group'])['total_cost'].sum().unstack()
print(financial_by_demographics)
print("-" * 50)

# 7. Correlation between Inventory Turnover and Expiry
print(" Correlation between Inventory Turnover and Expiry: ")
turnover_expiry_correlation = inventory_df[['turnover_rate', 'days_to_expiry']].corr().iloc[0, 1]
print(f"Correlation between Inventory Turnover Rate and Days to Expiry: {turnover_expiry_correlation:.2f}")
print("-" * 50)


# 8. Convert 'admission_date' and 'discharge_date' columns to datetime objects
patients_df['admission_date'] = pd.to_datetime(patients_df['admission_date'])
patients_df['discharge_date'] = pd.to_datetime(patients_df['discharge_date'])

# Calculate the length of stay in days
patients_df['calculated_length_of_stay'] = (patients_df['discharge_date'] - patients_df['admission_date']).dt.days


# Display a sample of the data to show the result
print("\nSample of data showing original and calculated length of stay:")
print(patients_df[['patient_id', 'admission_date', 'discharge_date', 'length_of_stay', 'calculated_length_of_stay']].head())

# Perform a quick check to see if the calculated and original values are consistent
are_consistent = (patients_df['length_of_stay'] - patients_df['calculated_length_of_stay']).abs().max() < 1
print(f"\nConsistency check between original and calculated length of stay: {are_consistent}")




