# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset, type(thisset)) 


# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) 


# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 


# Add elements from tropical into thisset
# The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 


# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) 



