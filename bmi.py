def calculate_bmi(height,weight):
    print("height = "+ str(height))
    print("weight = "+ str(weight))

    bmi = weight/(height * height)
    print("BMI = " + str(bmi))

    if bmi < 18:
     print("Underweight")
    elif 18.5 <= bmi <= 25.0:
       print("Normal")
    else:
       print("Overweight")

    calculate_bmi(height=57, weight=1.73)