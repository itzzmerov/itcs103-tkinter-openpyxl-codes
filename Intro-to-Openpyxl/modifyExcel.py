from openpyxl import load_workbook  

# Load an existing workbook
workbook = load_workbook("sample.xlsx")
sheet = workbook.active  # Get active sheet

# Modify cell values
sheet["B2"] = 26  # Change Alice's age

# Save changes
workbook.save("sample.xlsx")
print("Excel file updated successfully!")