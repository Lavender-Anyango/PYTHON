#!/usr/bin/python3

from datetime import datetime, timedelta


def age_Calculator(birthyear):

        
    # Get the current date
    now = datetime.now()

    # Ask the user for their date of birth

    # Calculate the difference between the current date and the birthday
    difference = now - birthday

    # Calculate the person's age in years
    age_in_years = difference.days // 365
 # Parse the user's input into a datetime object
dob_input = input("Enter your date of birth (YYYY-MM-DD):")
birthday = datetime.strptime(dob_input, "%Y-%m-%d")




age_Calculator(birthday)