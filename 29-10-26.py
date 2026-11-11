# 1.if statement
#1. positive no

no = int(input("Enter a number: "))

if no > 0:
    print("Positive Number")

# 2.voting

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")

#2.if else
#1.even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#2.pass or fail
marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")
#3.if elif else
#1.grade

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

#2.no
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#4.nested if
#1.login
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
     print("Login Successful")
    else:
      print("Incorrect Password")
else:
    print("Incorrect Username")
#2.largest 3 no's
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Largest number:", a)
    else:
        print("Largest number:", c)
else:
    if b >= c:
        print("Largest number:", b)
    else:
        print("Largest number:", c)

#5.ternary opr
# 1.maxof 2no
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = a if a > b else b

print("Largest number:", largest)
#2.age
age = int(input("Enter your age: "))

category = "Adult" if age >= 18 else "Minor"

print(category)


n=int(input())

if n%2==0:
    print("even")
else :
    print("odd")