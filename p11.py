# Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Total:", total)

# Example usage
sum_numbers(1, 2, 3)         
sum_numbers(10, 20, 30, 40)  
sum_numbers()                
