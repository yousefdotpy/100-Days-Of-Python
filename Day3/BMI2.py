# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(round((weight / height ** 2),0))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 :
    if bmi <= 25 :
        print(f"Your BMI is {bmi}, you have a normal weight.")
    if bmi > 25 and bmi <= 30 : 
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    if bmi >= 30 and bmi <35 :
        print(f"Your BMI is {bmi}, you are obes.")
else :
    print(f"Your BMI is {bmi}, you are clinically obese.")
