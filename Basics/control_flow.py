#!/usr/bin/python3

# working with if, elif and else statements 

def prices():
    age = int(input("Enter age: "))

    if age < 5:
        print("the ticket price will be $5")
    elif age >= 5 and age < 16:
        print("the ticket price $10")
    else:
        print("the price is $18")


prices()