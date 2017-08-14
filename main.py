import math

print("Hello World!")

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print (my_dict["fish"][0])



n = input("Enter a number ")
def myfunction(n):
    if type(n) == int and n % 3 == 0:
        return math.sqrt(n)
    else:
        print("Fail")

