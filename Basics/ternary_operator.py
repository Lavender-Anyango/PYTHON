#!/usr/bin/python3

# a concise way to write a conditional (if-else) statement
# syntax value_if_true if condition else value_if_false.

age = int(input("Enter age: "))
ticket_price = 20 if age >=18 else 5

print(f"The ticket price is {ticket_price}")