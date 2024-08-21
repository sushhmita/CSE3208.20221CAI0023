file1 = open("sample_data/My File.txt", "r")
text = file1.read()
print(text)
file2 = open("sample_data/My File.txt", "r")
lines = file2.readlines()
print(lines)
file_path="/content/data.tsv"
def count_lines(file_path):
    with open(file_path, 'r',errors="ignore") as file:
        lines = file.readlines()
        return len(lines)

line_count = count_lines(file_path)
print(f'The number of lines in the file is: {line_count}')
def count_fields(file_path):
    with open(file_path, 'r',errors="ignore") as file:
        first_line = file.readline().strip()
        fields = first_line.split()
        return len(fields)

file_path = '/content/data.tsv'
field_count = count_fields(file_path)
print(f'The number of fields in the first line is: {field_count}')
