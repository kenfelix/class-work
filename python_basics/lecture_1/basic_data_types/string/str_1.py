# Strings in python are used to represent unicode character values.

# declaring my first string variable

name = "Olamide Odunjo\U0001F600"

print(f"name is {name}, type is {type(name)}")


# multiline strings

multiline_with_newline_char = "heloo guy, welcome.\njeff bezos is our friend\n\n\tPrograming is so far awesome!!!"

print(multiline_with_newline_char)

multiline_str = """Heloo guy, welcome.
jeff bezos is our friend

    programming is so far awesome!!!"""

print(multiline_str)
