# Python Lists

# mylist = ["apple", "banana", "cherry"]

# print(mylist, type(mylist))

# mylist.append(34)

# print(mylist)

# mylist.pop(0)

# print(mylist)

# mylist.append(34)
# mylist.append("cherry")
# print(mylist, len(mylist))

# another_list = [1, 2.5, True, "miracle", [2, 4, 6, 8]]

# print(another_list)

# _list = list(("olamide", 1, 24, True))
# print(_list)

# first_item = mylist[-1]
# print(first_item)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 
print("berry" in thislist)

thislist[1] = [2, 4, 6, 8]

print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(0, 25.87)

print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


