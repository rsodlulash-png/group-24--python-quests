#!/usr/bin/python3
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

if operation == "add":
    print(add(num1, num2))
elif operation == "subtract":
    print(subtract(num1, num2))
elif operation == "multiply":
    print(multiply(num1, num2))
elif operation == "divide":
    print(divide(num1, num2))
else:
    print("Invalid operation!")
