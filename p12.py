# Write a program to display the use of local, global and nonlocal variables
x = 10

def outer():
    
    y = 5
    
    def inner():
        nonlocal y 
        global x 
        
        z = 2
        
        print("Inside inner()")
        print("Local z =", z)
        print("Nonlocal y before change =", y)
        print("Global x before change =", x)
        
        y += 10
        x += 20
        print("Nonlocal y after change =", y)
        print("Global x after change =", x)
    
    inner()
    print("Inside outer() after inner()")
    print("Nonlocal y in outer() =", y)

outer()
print("Outside all functions, global x =", x)
