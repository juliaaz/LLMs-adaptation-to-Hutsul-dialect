import json
from sklearn.model_selection import train_test_split

def split_and_save_json(input_file, train_output_file, test_output_file, test_size=0.2, random_state=42):
    with open(input_file, 'r', encoding='utf-8') as file:
        dataset = json.load(file)

    # Splitting the data into training and testing sets
    train_data, test_data = train_test_split(dataset, test_size=test_size, random_state=random_state)

    print("Train set size:", len(train_data))
    print("Test set size:", len(test_data))

    # Save training data to a new JSON file
    with open(train_output_file, 'w', encoding='utf-8') as file:
        json.dump(train_data, file, ensure_ascii=False, indent=4)

    # Save test data to a new JSON file
    with open(test_output_file, 'w', encoding='utf-8') as file:
        json.dump(test_data, file, ensure_ascii=False, indent=4)

# Example usage:
split_and_save_json('ivanchyk.json', 'train_ivanchyk.json', 'test_ivanchyk.json')
