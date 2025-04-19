# Open file in read mode ('r') and read content
file = open("example.txt", "r")
content = file.read()
file.close()  # Always close the file
print("File Content:\n", content)