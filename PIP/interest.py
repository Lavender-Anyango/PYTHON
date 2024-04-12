def interest_calc(principle, interest_rate, time):
    simple_interest = (principle * interest_rate * time) / 100
    total_amount = simple_interest + principle
    print(total_amount)

# Correctly define the variables before calling the function
principle = float(input("Enter the principle: "))
interest_rate = float(input("Enter the interest: "))
time = float(input("Enter the time: "))

# Now call the function with the correctly defined variables
interest_calc(principle, interest_rate, time)