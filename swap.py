# Swap two numbers without using a third variable.

print("\n Enter Values to Swap...")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a
print("\n After swapping...")
print("a =", a)
print("b =", b)
