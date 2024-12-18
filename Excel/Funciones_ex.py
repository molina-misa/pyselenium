import openpyxl
from openpyxl.workbook import Workbook



class ExcelFunction:
    def __init__(self, driver):
        self.driver = driver

    def getRowCount(file,path,sheetName):
        Workbook = openpyxl.load_workbook(path)
        sheet = Workbook[sheetName]
        return sheet.max_row

    def getColumnCount(file,sheetName):
        Workbook = openpyxl.load_workbook(file)
        sheet = Workbook[sheetName]
        return sheet.max_column

    def readData(file,path,sheet_name,row_num,colum_num):
        Workbook = openpyxl.load_workbook(path)
        sheet = Workbook[sheet_name]
        return sheet.cell(row = row_num, column = colum_num).value

    def writeData(file,path,sheet_name,row_num,colum_num,data):
        Workbook = openpyxl.load_workbook(path)
        sheet = Workbook[sheet_name]
        sheet.cell(row = row_num, column = colum_num).value = data
        Workbook.save(path)

    