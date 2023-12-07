import pyinputplus as pyip

def getBMI(height:float, weight:float) -> tuple[float,str]:
    BMI = weight / (height*0.01)**2
    message = ""
    if BMI < 18.5:
        message = "「您的體重過輕」"
    elif BMI < 24:        
        message = "「您的體重正常」"
    
    elif BMI < 27:        
        message = "「您的體重過重」"

    elif BMI < 30:        
        message = "「您的體重輕度肥胖」"

    elif BMI < 35:        
        message = "「您的體重中度肥胖」"

    else:        
        message = "「您的體重重度肥胖」"

    return (BMI,message)

    


h = pyip.inputFloat("請輸入身高，單位為公分:",min = 0)
print(h)
w = pyip.inputFloat("請輸入體重，單位為公斤:",min = 0)
print(w)
bmi, message = getBMI(height=h,weight=w)
print(f"您的BMI是{bmi:.2f},{message}")
