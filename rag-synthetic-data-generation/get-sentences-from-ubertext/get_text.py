import re
import os

def extract_first_sentences(input_filename, output_filename, sentence_count):
    sentence_endings = re.compile(r'[.!?]\s+')
    extracted_sentences = []

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            print(f"Reading from {input_filename}...")

            for line in infile:
                sentences = sentence_endings.split(line)
                for sentence in sentences:
                    extracted_sentences.append(sentence.strip())
                    
                    # Check if we have reached the desired number of sentences
                    if len(extracted_sentences) >= sentence_count:
                        break
                
                if len(extracted_sentences) >= sentence_count:
                    break

        output_content = '|!|'.join(extracted_sentences[:sentence_count])

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            print(f"Writing to {output_filename}...")
            outfile.write(output_content)
        
        print(f"{len(extracted_sentences)} sentences have been successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def split_file(input_filename, output_filename1, output_filename2, split_index):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read().split('|!|')
        
        first_part = '|!|'.join(content[:split_index])
        second_part = '|!|'.join(content[split_index:])
        
        with open(output_filename1, 'w', encoding='utf-8') as outfile1:
            outfile1.write(first_part)
        
        with open(output_filename2, 'w', encoding='utf-8') as outfile2:
            outfile2.write(second_part)
        
        print(f"The file {input_filename} has been successfully split into {output_filename1} and {output_filename2}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Step 1: Extract 500k sentences into one file
    extract_first_sentences('ubertexts/ubertext.fiction.filter_rus_gcld+short.text_only.txt', 'fiction-250k.txt', 250000)
