# Student Grade Calculator

print("Welcome to Grade Calculator!")
name = input("Enter Your Name: ")
sub1 = int(input("Enter 1st Subject: "))
sub2 = int(input("Enter 2nd Subject: "))
sub3 = int(input("Enter 3rd Subject: "))

avg = (sub1 + sub2 + sub3) / 3

if avg > 80:
    grade = "A+"
elif avg < 80 and avg > 70:
    grade = "A"
elif avg < 70 and avg > 60:
    grade = "B"
else:
    grade = "C"

print(avg)
print(f"Grade For {name} is: {grade}")
