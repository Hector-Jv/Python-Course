def add(x, y):
    return x + y

# With lists
numbers = [10, 14]
add_numbers = add(*numbers)

# With dicts
numbers_dict = {
    "x": 10,
    "y": 14
}
# First form
add_numbers = add(x = numbers_dict["x"], y = numbers_dict["y"])
# Second form
add_numbers = add(**numbers_dict)

