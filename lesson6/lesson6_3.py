from pprint import pprint
import tools

def main():
    sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
    print(sitenames)
  

if __name__ == '__main__':
    main()