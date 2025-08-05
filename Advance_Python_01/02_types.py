from typing import List, Union, Tuple

n : int = 5             # identify n is integer

name: str = "Harry"         # identify name is string

def  sum(a: int, b: int) -> int:        # a = integer, b = integer, return = integer
    return a+b

print(sum(3,6))

number : List = [1,5,7,8]
print(number)

person: Tuple[str, int] = ("Shuvo", 5)
print(person)

