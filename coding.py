# Basic Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculation based on the operation
sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined"
# Display the result

print(f"Sum: {sum}")  # +
print(f"Difference: {subtraction}")  # _
print(f"Product: {multiplication}")  # 
print(f"division: {division}")  # / if num2 != 0 else "undefined"  # /