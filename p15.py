# create user defined exception
class MyError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise MyError("Negative numbers are not allowed")
    
    print("You entered:", num)

except MyError as e:
    print("User Defined Exception:", e)