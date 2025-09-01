file_path = input("Enter the file path and filename (e.g., /path/to/yourfile.txt): ")
text = input("Enter the text to write to the file: ")
with open(file_path, 'w') as file:
    file.write(text)
print(f"Text has been written to {file_path}")
