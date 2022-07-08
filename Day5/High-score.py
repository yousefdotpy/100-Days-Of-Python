# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = student_scores[0]
for high in student_scores:
    if high > max:
        max = high
    else:
        continue
print(f"The highest score in the class is: {max}")
