# Write a program to create 4 lambda functions which shall accept 
# 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Division by zero"

# Function to perform operation based on operator
def calculate(a, b, operator):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        return "Invalid operator"

# Example usage
print(calculate(10, 5, '+'))  
print(calculate(10, 5, '-'))  
print(calculate(10, 5, '*'))  
print(calculate(10, 5, '/'))  
print(calculate(10, 0, '/'))  
print(calculate(10, 5, '^'))  
