# Basic Exception Handling Example

try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers only.")

else:
    # Executes if no exception occurs
    print("Result:", result)

finally:
    # Always executes
    print("Program execution completed.")