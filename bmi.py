def calculate_bmi(height,weight):
    print("height = "+ str(height))
    print("weight = "+ str(weight))

    bmi = weight/(height * height)
    print("BMI = " + str(bmi))

    if bmi < 18:
     print("Underweight")
     return -1
    elif 18.5 <= bmi <= 25.0:
       print("Normal")
       return 0
    else:
       print("Overweight")
       return 1

    #calculate_bmi(height=57, weight=1.73)