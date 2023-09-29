# match statement

"""
match <condition>:
    case <value>:
        <command>
    .
    .
    .
    case _:
      <command>

"""


a = 33
b = 33

match a:
    case 1:
        print("a is equal to 1")
    case _:
      print("a is not equal to 1")

match b > a:
    case True:
        print("b is greater than a")
    case False:
        print("not in this scope")
    case _:
      print("a is not equal to 1")