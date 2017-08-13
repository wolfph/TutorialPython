import math

print("Hello World!")

n = input("Enter a number ")
def myfunction(n):
    if type(n) == int and n % 3 == 0:
        return math.sqrt(n)
    else:
        print("Fail")