from pprint import pprint
import openpyxl
from openpyxl import Workbook,worksheet
import tools

def main():
    sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
    wb:Workbook = openpyxl.Workbook()
    sheet:worksheet = wb.active
    sheet.title = "站點名稱"
    for idy ,name in enumerate(sitenames):
        print(name)
        sheet.cell(column=1,row=idy+1,value=name)
    wb.save('老板要的資訊.xlsx')
  

if __name__ == '__main__':
    main()