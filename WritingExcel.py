import openpyxl

path="D:\\Timesheet SMM\\1. Afina Putri Dayanti - Mei.xlsx"

workbook = openpyxl.load_workbook(path)

sheet= workbook.active

for r in range(6,10):
    for c in range(5,6) :
        sheet.cell(row=r, column=c).value="test"

workbook.save(path)