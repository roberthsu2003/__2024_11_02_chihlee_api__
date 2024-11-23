PI=3.1415926

class Person:
    pass

def get_status(bmi:float)->str:
    '''
    docstring
    Parameter:
        bmi:bmi值可以整數或浮點數
    Return:str
        會傳出5個狀態
        - 正常範圍
        - 過重 
        - 輕度肥胖      
    '''
    if bmi >= 35 :
        bmi_str = '重度肥胖'
    elif bmi >= 30 :
        bmi_str = '中度肥胖'
    elif bmi >= 27 :
        bmi_str = '輕度肥胖'
    elif bmi >= 24 :
        bmi_str = '過重'
    elif bmi >= 18.5 :
        bmi_str = '正常範圍'
    else :
        bmi_str = '過輕' 
    return bmi_str
    
def BMI_math(height_cm:float, weight_kg:float)->tuple[float,str]:
    height_m = round(height_cm/100, 2)
    bmi_kg_m2 = round(weight_kg/(height_m**2), 2)
    bmi_str = get_status(bmi_kg_m2)
    return bmi_kg_m2, bmi_str