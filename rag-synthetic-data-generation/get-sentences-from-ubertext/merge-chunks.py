import pandas as pd
import os

# Path to the directory containing the CSV files
directory = 'finction_chunks'

# List to store DataFrames from each CSV file
dfs = []

# Read each CSV file and append its DataFrame to the list
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        dfs.append(df)

# Concatenate all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

# Sort the DataFrame by the "Count" column in descending order
sorted_df = merged_df.sort_values(by='Count', ascending=False)

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv('merged_fiction-250k.csv', index=False)

print("Merged and sorted CSV file saved as 'merged_fiction-250k.csv'.")
