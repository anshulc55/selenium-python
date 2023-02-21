import openpyxl
import os
import time

# Write Excel Files
path = os.getcwd()+"/FileData/sample.xlsx"
wb = openpyxl.Workbook()

sheet = wb.active
sheet["A1"] = 123
sheet["A2"] = "Tokyo"
sheet["A3"] = 12.65
sheet["A4"] = 90

date = time.strftime("%x")
sheet["A5"] = date

wb.save(path)