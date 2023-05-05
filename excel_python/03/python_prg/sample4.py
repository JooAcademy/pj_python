import openpyxl


wb = openpyxl.load_workbook("..\data\sample1.xlsx")
for sheet in wb:
    for row in sheet:
        for cell in row:
            print(cell.value)
