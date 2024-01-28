def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1)) #5*4*3*2*1

num = 5
print("The factorial of", num, "is", factorial(num))
