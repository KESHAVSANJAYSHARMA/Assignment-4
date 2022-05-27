#Assignment 4
#Name: Keshav Sharma
#SID: 21107092
#Branch: Mechanical Engineering

#Q1
print("Q1")
print("This program gives your grade according to your marks.")
#User inputs marks
secured_marks = float(input("Enter your marks: "))

if secured_marks < 25:
    print("Your grade is F")

elif 25 <= secured_marks < 45:
    print("Your grade is E")
                    
elif 45 <= secured_marks < 50:
    print("Your grade is D")

elif 50 <= secured_marks < 60:
    print("Your grade is C")

elif 60 <= secured_marks < 80:
    print("Your grade is B")

else:
    print("Your grade is A")

#Q2

print('Q2')
year = int(input('Enter year:'))
if year % 4 == 0:
    if year % 100 == 0:
        print("Leap year")

    else:
        print("Not a leap year")

else:
    print("Not a leap year")

#Q3

print('Q3')
import random
print("Multiplication game program for kids.")
for i in range(1,11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}:{a}x{b}='))
    if ans == a*b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a*b)

#Q4

print('Q4')
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:",i)
