def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi=weight/(height*height)
#Add code here to display calculate BMI
    if bmi <18.5:
        print("You skinny as hell")
    elif 18.5<bmi<=24.9:
        print("You healthy")
    elif 24.9<bmi<=29.9:
        print("You fat")
    else:
        print("You fat as hell")
    print("Your BMI is: ",bmi)

calculate_bmi(weight=57, height=1.73)