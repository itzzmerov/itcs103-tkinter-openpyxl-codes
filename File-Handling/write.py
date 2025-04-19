# Open a file in write mode ('w') and add content
file = open("example.txt", "w")  
file.write("Hello, this is a file handling example.\n")
file.write("Python makes file handling easy!")
file.close()  # Always close the file
print("File written successfully!")