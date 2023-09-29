# # Python Logical Operators

# print(2 > 4 and 2 < 4) # false
# print(2 > 1 and 5 < 10) # true

# print(2 > 4 or 2 < 4) # true
# print(2 > 1 or 5 < 10) # true
# print(3 == 3 or 4 ==4 or 5 == 9 or 4 > 29)  # true

# print((3==1 or 1==1) and (4>2 or 2>3))


# print(not 3==1)




# # Python Identity Operators

# x = [1, 2]
# y = [1, 2]
# print(x is y)
# print(x == y)

# a = 2
# b = 2.0

# print(a is b)
# print(a == b)




# # Python Membership Operators

# name = "Olamide Odunjo"

# print("Odunj" in name)
# print("OdunJ" not in name)




# Python Bitwise Operators

print(1000 & 23456) # prints 928
"""
0000001111101000
0101101110100000
--------------------
0000001110100000

"""

print(1000 | 23456)  # prints 23528
"""
0000001111101000
0101101110100000
--------------------
0101101111101000

"""

print(1000 ^ 23456)  # prints 22600
"""
0000001111101000
0101101110100000
--------------------
0101100001001000

"""

print(~10)  # prints -11
"""
01010
--------------------
10101

"""