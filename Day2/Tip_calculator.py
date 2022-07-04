
#Write your code below this line 👇
print("It's yousefdotpy, Welcome to the tip calculator")
bill = float(input("What was the total bill ? $"))
percentage = float(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tips = (percentage / 100 * bill + bill)
total = round((tips / people),2)
print(f"Each person should pay: $ {total}")
