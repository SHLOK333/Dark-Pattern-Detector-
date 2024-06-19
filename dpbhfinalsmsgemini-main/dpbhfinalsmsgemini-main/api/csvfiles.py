import csv

# Your obtained data
result_data = ['Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Social Proof', 'Not Dark', 'Obstruction', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Not Dark', 'Urgency']

# Specify the file names
csv_file_name = 'output.csv'
text_file_name = 'output.txt'

# Writing to CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Result'])  # Writing header
    csv_writer.writerows([[item] for item in result_data])

# Writing to text file
with open(text_file_name, 'w') as text_file:
    text_file.write('\n'.join(result_data))

print(f'Data written to {csv_file_name} and {text_file_name}')
