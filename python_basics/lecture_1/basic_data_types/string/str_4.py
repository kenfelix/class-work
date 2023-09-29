#  String Concatenation

a = "Hello"
b = "World"
num = 1
# print(a + " " + b)


# String Formating

print("the computer is saying {} {:.10f}".format(a, num))

print(f"the computer is saying {a} {b}")


# escape characters \

print("\"The Porcelain Village\" by Jonathan Page\nThe deafening ringing in my ears seemed to be louder than my own thoughts. I knew something was wrong, but not this wrong.")

import time

print("l", end="\r")
time.sleep(3)
print("lo", end="\r")
time.sleep(3)
print("loa", end="\r")
time.sleep(3)
print("load", end="\r")
time.sleep(3)
print("loadi", end="\r")
time.sleep(3)
print("loadin", end="\r")
time.sleep(3)
print("loading", end="\r")
time.sleep(3)
print("loading.", end="\r")
time.sleep(3)
print("loading..", end="\r")
time.sleep(3)
print("loading...")



