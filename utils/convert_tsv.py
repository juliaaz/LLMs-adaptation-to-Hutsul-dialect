import csv

def read_input_file(file_path):
    """Reads the input file and returns a list of lines."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def write_to_csv(lines, output_file):
    """Writes the lines into a CSV file."""
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Hutsul', 'Ukrainian'])

        for line in lines:
            parts = line.strip().split('    ')
            writer.writerow(parts[:2])

def convert_to_csv(input_file, output_file):
    """Converts the input file to CSV."""
    lines = read_input_file(input_file)
    write_to_csv(lines, output_file)

convert_to_csv('маловживані.txt', 'маловживані.csv')
