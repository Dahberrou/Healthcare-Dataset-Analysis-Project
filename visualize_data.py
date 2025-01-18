import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("/Users/apple/healthcare-project1/data/cleaned_healthcare.csv")

# Convert 'DATE' column to datetime with the correct format
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y')
df.set_index('DATE', inplace=True)

# Plot total cases over time and save the plot
df['TOTAL_CASES'].plot(title="Total Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.savefig("/Users/apple/healthcare-project1/plots/total_cases_over_time.png")  # Use absolute path
plt.show()

# Heatmap of correlations (exclude non-numeric columns)
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("/Users/apple/healthcare-project1/plots/correlation_heatmap.png")  # Use absolute path
plt.show()
