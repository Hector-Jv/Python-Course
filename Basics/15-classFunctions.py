def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 15, operator=divide)
print(result)




####################################

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Adolfo", "age": 25},
    {"name": "Luis", "age": 30},
]

def get_friend_name(friend):
    return friend["name"]

# 1 
print(search(friends, "Bob", get_friend_name))
# 2
print(search(friends, "Bob", lambda friend: friend["name"]))
# 3
from operator import itemgetter
print(search(friends, "Bob", itemgetter("name")))

