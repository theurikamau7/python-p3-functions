#!/usr/bin/env python3

# Question 1
def greet_programmer():
   print("Hello, programmer!")


# Question 2
def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")


# Question 3
def greet_with_default(name = "programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")


# Question 4
def add(num1, num2):
    sum = num1 + num2
    return sum

result = add(5, 10)
print(result)


# Question 5
def halve(input_value):
    if type(input_value) in (int, float):
        return input_value / 2
    else:
        return None

result = halve(4)
print(result)

result = halve("two")
print(result)