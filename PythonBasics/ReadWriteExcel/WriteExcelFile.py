import openpyxl
import os

file_path = os.getcwd()+"/FileData/ExecelSampleFile1.xlsx"
wb = openpyxl.Workbook()
sheet = wb.active

# Write in a Specific Cell
'''
sheet["A1"] = "Hello"
sheet["E7"] = "Team"
sheet.cell(row=3, column=3).value = 1000
'''

# Write multiple Columns and Rows
data = (
    ("EMPLOYEE NAME", "DEPARTMENT", "BRANCH", "RANK"),
    ("Andrew", "Forensic", "New York", 5),
    ("Mark", "Food", "Tokyo", 2),
    ("Julia", "Forensic", "New York", 2),
    ("Stephen", "Legal", "LA", 1),
    ("Bharat", "Food", "Tokyo", 2),
    (100, 23, 4543, 32, 43, 44)
)

for row in data:
    sheet.append(row)

wb.save(file_path)
