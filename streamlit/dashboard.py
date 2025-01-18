import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("/Users/apple/healthcare-project1/data/cleaned_healthcare.csv")

# Title
st.title("Healthcare Dataset Dashboard")

# Sidebar filters
county = st.sidebar.selectbox("Select County", df['COUNTY'].unique())
filtered_data = df[df['COUNTY'] == county]

# Display filtered data
st.write("Filtered Data:", filtered_data)

# Plot total cases over time
st.subheader("Total Cases Over Time")
fig, ax = plt.subplots()
filtered_data.set_index('DATE')['TOTAL_CASES'].plot(ax=ax)
st.pyplot(fig)

# Heatmap of correlations
st.subheader("Correlation Heatmap")
numeric_df = filtered_data.select_dtypes(include=['float64', 'int64'])
fig, ax = plt.subplots()
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
