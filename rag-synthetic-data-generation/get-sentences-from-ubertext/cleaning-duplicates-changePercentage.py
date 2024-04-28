import pandas as pd

sorted_df = pd.read_csv('sorted_with_percentage_fiction-250k.csv')
filtered_df = sorted_df[(sorted_df['NumWords'] >= 4) & (sorted_df['ChangedWordsPercentage'] > 0)]


filtered_df = filtered_df.sort_values(by='ChangedWordsPercentage', ascending=False)
filtered_df_no_duplicates = filtered_df.drop_duplicates()
filtered_df_no_duplicates.to_csv('filtered_and_sorted_no_duplicates-fiction-250k.csv', index=False)

print("Filtered, sorted, and duplicate rows removed. CSV file saved as 'filtered_and_sorted_no_duplicates-fiction-250k.csv'.")
