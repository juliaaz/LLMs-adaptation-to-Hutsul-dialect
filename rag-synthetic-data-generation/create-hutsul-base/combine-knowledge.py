import json
import csv

with open('hutsul-base/ivanchyk.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

hutsul_sentences = [entry['hutsul'] for entry in data]

with open('hutsul-base/combined_essays_split.txt', 'r', encoding='utf-8') as essays_file:
    combined_essays_sentences = [line.strip() for line in essays_file if line.strip()]

with open('hutsul-base/u_nas_hutsuliv_sentences.txt', 'r', encoding='utf-8') as hutsul_sentences_file:
    u_nas_hutsuliv_sentences = [line.strip() for line in hutsul_sentences_file if line.strip()]

all_sentences = hutsul_sentences + combined_essays_sentences + u_nas_hutsuliv_sentences

# Write data to CSV file
with open('hutsul-base.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['hutsul_sentence'])
    writer.writerows([[sentence] for sentence in all_sentences])
