import streamlit as st
import pandas as pd

st.title("Coffee Sales Dashboard")

file_path = "sales.csv"

try:
    sales_data = pd.read_csv(file_path)

    sales_data['date'] = pd.to_datetime(sales_data['date'], errors='coerce')
    sales_data['money'] = pd.to_numeric(sales_data['money'], errors='coerce')

    st.write("### Filter Data by Date")
    min_date = sales_data['date'].min()
    max_date = sales_data['date'].max()
    start_date, end_date = st.date_input(
        "Select date range:",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    filtered_data = sales_data[(sales_data['date'] >= pd.Timestamp(start_date)) & (sales_data['date'] <= pd.Timestamp(end_date))]

    st.write("### Data Preview")
    st.dataframe(filtered_data)

    total_revenue = filtered_data['money'].sum()
    avg_revenue = filtered_data['money'].mean()
    unique_coffees = filtered_data['coffee_name'].nunique()

    st.write("### Key Performance Indicators (KPIs)")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
    col2.metric(label="Average Revenue per Sale", value=f"${avg_revenue:,.2f}")
    col3.metric(label="Unique Coffee Types", value=unique_coffees)

    st.write("### Revenue Over Time")
    if 'date' in filtered_data.columns:
        daily_revenue = filtered_data.groupby('date')['money'].sum().reset_index()
        daily_revenue = daily_revenue.rename(columns={'date': 'Date', 'money': 'Revenue'})
        st.line_chart(daily_revenue.set_index("Date"))

    st.write("### Revenue Distribution")
    revenue_grouped = filtered_data.groupby(filtered_data['date'].dt.to_period('M'))['money'].sum().reset_index()
    revenue_grouped.columns = ['Month', 'Revenue']
    revenue_grouped['Month'] = revenue_grouped['Month'].astype(str)
    st.bar_chart(revenue_grouped.set_index("Month"))

except FileNotFoundError:
    st.error(f"File not found: {file_path}. Please make sure the path is correct.")
except pd.errors.EmptyDataError:
    st.error(f"The file {file_path} is empty.")
except pd.errors.ParserError:
    st.error(f"Error parsing the file {file_path}. Please check its format.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")