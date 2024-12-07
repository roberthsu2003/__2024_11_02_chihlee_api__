from openpyxl import load_workbook, Workbook, worksheet

def get_aqi(excel_name:str) -> list[dict]:
    wb:Workbook = load_workbook(excel_name)
    from pprint import pprint
    sheet:worksheet = wb.worksheets[0]
    sheets:list = []
    column_names:list[str] =[cell.value for cell in list(sheet)[0]]
    for row in list(sheet)[1:]:
        site:dict = {column_names[idx]:cell.value for idx,cell in enumerate(row)}    
        sheets.append(site)

    return sheets

def get_sitenames(excel_name:str) -> list[str]:
    data:list[dict] = get_aqi(excel_name=excel_name)
    sitenames:list = []
    for item in data:
        sitenames.append(item['sitename'])    

    sitenames = list(set(sitenames))
    return sitenames