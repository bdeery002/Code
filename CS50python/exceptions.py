import sys

# First try-except block: Handle invalid numeric input

try:
    x = int(input("Enter a number: "))
    y =int(input("Enter another number: "))

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
    sys.exit(1)
    
# Second try-except block: Handle division by zero
try:
    result = x / y
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
    sys.exit(1)

print(f"The result of {x} divided by {y} is {result}")