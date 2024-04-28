import pandas as pd

# Function to count the number of words in a sentence
def count_words(sentence):
    return len(sentence.split())

# Function to count the number of changed words based on 'Found Phrases'
def count_changed_words(found_phrases):
    # Check if found_phrases is a string, if not return 0
    if isinstance(found_phrases, str):
        return found_phrases.count('|') + 1  # Assuming '|' is the separator between phrases
    else:
        return 0


if __name__ == "__main__":
    # Read the merged and sorted CSV file
    merged_sorted_df = pd.read_csv('merged_fiction-250k.csv')

    merged_sorted_df['NumWords'] = merged_sorted_df['Sentence'].apply(count_words)
    merged_sorted_df['ChangedWords'] = merged_sorted_df['Found Phrases'].apply(count_changed_words)

    # Calculate the percentage of changed words and create a new column 'ChangedWordsPercentage'
    merged_sorted_df['ChangedWordsPercentage'] = (merged_sorted_df['ChangedWords'] / merged_sorted_df['NumWords']) * 100

    # Sort the DataFrame by 'ChangedWordsPercentage' in descending order
    sorted_df = merged_sorted_df.sort_values(by='ChangedWordsPercentage', ascending=False)
    sorted_df.to_csv('sorted_with_percentage_fiction-250k.csv', index=False)

    print("Sorted CSV file with percentages saved as 'sorted_with_percentage_fiction-250k.csv'.")
