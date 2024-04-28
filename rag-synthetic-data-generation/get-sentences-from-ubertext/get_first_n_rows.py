import pandas as pd

input_file_path = 'filtered_and_sorted_no_duplicates-fiction-250k.csv'
output_file_path = 'fiction-10k.csv'

df = pd.read_csv(input_file_path, nrows=10000)
df.to_csv(output_file_path, index=False)

print("First 10,000 rows have been saved to the new CSV file.")
