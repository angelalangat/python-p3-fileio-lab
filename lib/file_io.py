def write_file(file_name, file_content):
    file_name = f"{file_name}.txt"  # Add .txt extension
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = f"{file_name}.txt"  # Add .txt extension
    with open(file_name, 'a') as file:
        file.write(append_content)  # Changed file_content to append_content

def read_file(file_name):
    file_name = f"{file_name}.txt"  # Add .txt extension
    with open(file_name, 'r') as file:
        return file.read()
