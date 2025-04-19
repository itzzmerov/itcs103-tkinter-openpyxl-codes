from openpyxl import Workbook  

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active  # Get the active sheet

# Write data into cells
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["A2"] = "Alice"
sheet["B2"] = 25
sheet["A3"] = "Bob"
sheet["B3"] = 30

# Save the workbook
workbook.save("sample.xlsx")
print("Excel file created successfully!")