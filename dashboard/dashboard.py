import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Visualisasi Data - Ryan Hangralim")
st.subheader("Top 10 kategori dengan penjualan tertinggi")
category = pd.read_csv('../data/top_10_category.csv')
sorted_category = category.sort_values(by='count', ascending=False)

# Create a horizontal bar chart
plt.figure(figsize=(10, 6)) 
plt.barh(sorted_category['product_category_name'], sorted_category['count'])
plt.xlabel('Count')
plt.ylabel('Name')
plt.title('Top 10 Product Categories')
plt.gca().invert_yaxis() 

# Show the plot
st.pyplot(plt)


st.subheader("Perbandingan frekuensi metode pembayaran")
payment = pd.read_csv('../data/payment_counts.csv')

plt.figure(figsize=(8, 8))
plt.pie(
    x=payment['count'],
    labels=payment['method'],
    autopct='%1.1f%%',
)
plt.title('Payment Method Comparison')
plt.axis('equal')

# Show the plot in Streamlit
st.pyplot(plt)