from ExcelUtil import ReadWriteExcel

fileName="StudentData.xlsx"
sheetName = "StudentData"

excel_file = ReadWriteExcel(fileName)

'''
excel_file = ReadWriteExcel(fileName)
print(excel_file.readby_columnIndex(sheetName, 2, 3))
print(excel_file.readby_columnName(sheetName, 4, "BRANCH"))
print("Total Rows in My Sheet - ", excel_file.get_totalRows(sheetName))
print("Total Columns in My Sheet - ", excel_file.get_totalColumn(sheetName))
'''

excel_file.writeby_columIndex(sheetName, 4, 3, "Electronics and Communications")

# Read the Names Column
for cell in range(2, excel_file.get_totalRows(sheetName)+1):
    print(excel_file.readby_columnName(sheetName, cell, "COURSE"))


