from pprint import pprint
import tools

def main():
    data:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')
    sitenames:list = []
    for item in data:
        sitenames.append(item['sitename'])    

    sitenames = list(set(sitenames))
    print(len(sitenames))

if __name__ == '__main__':
    main()