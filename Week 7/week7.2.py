source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    content = src.read()
    dest.write(content.lower())
print(f"Content copied from {source_file} to {destination_file} in lowercase.")
