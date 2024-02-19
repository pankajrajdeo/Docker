import os
import collections
import socket

# Ensure the output directory exists
output_dir = '/home/output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to count words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words), collections.Counter(words)

# List all text files in /home/data
text_files = [f for f in os.listdir('/home/data') if f.endswith('.txt')]
initial_output = f"Text files: {text_files}\n"

# Initialize variables for detailed output
total_words = 0
word_counts = collections.Counter()
details_output = "Text files: " + ", ".join(text_files) + "\n"

# Process each text file
for file_name in text_files:
    file_path = os.path.join('/home/data', file_name)
    words_count, words_counter = count_words_in_file(file_path)
    total_words += words_count
    details_output += f"{file_name}: {words_count} words\n"
    if file_name == 'IF.txt':
        word_counts = words_counter

# Top 3 words in IF.txt
top_three = word_counts.most_common(3)
top_three_output = "Top 3 words in IF.txt: " + ", ".join([f"{word} ({count})" for word, count in top_three]) + "\n"

# Find the IP address
ip_address = socket.gethostbyname(socket.gethostname())
ip_output = f"IP Address: {ip_address}\n"

# Combine all parts of the output
final_output = initial_output + top_three_output + ip_output + details_output
final_output += f"Total words: {total_words}\n" + top_three_output + ip_output

# Write the results to a file and print to console
with open('/home/output/result.txt', 'w') as output_file:
    output_file.write(final_output)

print(final_output)
