import tools
def main():
    while(True):
        try:
            height_cm = float(input("請輸入身高(公分):"))
            weight_kg = float(input("請輸入體重(公斤):"))
            bmi_value, bmi_str = tools.BMI_math(height_cm, weight_kg)
            break
        except Exception:
            print('輸入格式錯誤,請重新輸入!')
        
    print(f"您的BMI值是{bmi_value}\n您的體重{bmi_str}")
    print("程式結束")

if __name__ == '__main__':
    main()
    
