import pandas as pd

# Load the dataset
df = pd.read_csv("~/healthcare-project1/data/healthcare-project1.csv")

# Handle missing values
df.fillna(0, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv("~/healthcare-project1/data/cleaned_healthcare.csv", index=False)
