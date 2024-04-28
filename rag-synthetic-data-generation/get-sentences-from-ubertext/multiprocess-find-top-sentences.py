import csv
import re
import time
from multiprocessing import Pool

def load_ukrainian_phrases(csv_filename):
    """Load Ukrainian phrases from a CSV file."""
    phrases = set()
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phrases.add(row['Ukrainian'].lower())
    return phrases

def process_sentences(chunk):
    """Process a chunk of sentences and count occurrences of dictionary phrases."""
    results = []
    sentences, phrases_set, output_filename, total_sentences = chunk
    processed_sentences = 0
    
    start_time = time.time()
    last_log_time = start_time
    
    for sentence in sentences:
        if sentence.strip():  # Ensure the sentence is not just whitespace
            normalized_sentence = sentence.lower()
            found_phrases = []
            for phrase in phrases_set:
                if re.search(r'\b' + re.escape(phrase) + r'\b', normalized_sentence):
                    found_phrases.append(phrase)
            
            phrase_count = len(found_phrases)
            
            results.append((sentence.strip(), phrase_count, found_phrases))
            
            processed_sentences += 1
            
            # Check if 2 minutes have passed since the last log
            if time.time() - last_log_time >= 120:
                elapsed_time = time.time() - start_time
                progress = int(processed_sentences / total_sentences * 100)
                print(f"Processed {progress}% of 250,000 sentences in {elapsed_time:.2f} seconds")
                last_log_time = time.time()

    save_results(results, output_filename)

def save_results(results, output_filename):
    """Save the results to a new file."""
    with open(output_filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Sentence', 'Count', 'Found Phrases'])
        for sentence, count, found_phrases in results:
            writer.writerow([sentence, count, '|'.join(found_phrases)])

if __name__ == "__main__":
    ukrainian_phrases = load_ukrainian_phrases('hutsul-ukrainian-dictionary.csv')
    with open('fiction-250k.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    chunk_size = 25000
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    total_sentences = len(content.split('|!|'))

    with Pool(processes=10) as pool:
        chunk_data = [(chunk.split('|!|'), ukrainian_phrases, f'finction_chunks/output_fiction-{i}.csv', total_sentences) for i, chunk in enumerate(chunks, start=1)]
        pool.map(process_sentences, chunk_data)

    print("Processing complete. Results saved to 'output_1.csv' through 'output_10.csv'.")
