import os  

# Get current directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Check if file exists before reading
file_path = os.path.join(current_directory, "example.txt")
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print("File Content:\n", file.read())
else:
    print("File does not exist!")