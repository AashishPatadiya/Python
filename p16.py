#generate arithmetic exception
import logging

# configure logging
logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b   # may cause arithmetic exception
    print("Result:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception occurred!")
    logging.error("Exception occurred: %s", e)