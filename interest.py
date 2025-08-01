# Program to Calculate simple interest.

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (in %): "))
time = float(input("Enter Time (in years): "))
simple_interest = (principal * rate * time) / 100
print(f"\nSimple Interest = {simple_interest}")
print(f"Total Amount after {time} years = {principal + simple_interest}")
