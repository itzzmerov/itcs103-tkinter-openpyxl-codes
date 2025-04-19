# create_excel_file.py
from openpyxl import Workbook

# Create a workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "UserData"

# Add headers
ws.append(["Name", "Email", "Date of Birth"])

# Save the file
wb.save("userdata.xlsx")
print("Excel file created successfully.")
