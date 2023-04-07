# add, order, delete, modify, consult, unrepeat
list = ["Element 1", "Element 2", "Element 3"]
# order, consult, repeat
tuple = ("Element 1", "Element 2", "Element 3")
# unordered, add, delete, unrepeat, consult
set = {"Element 1", "Element 2", "Element 3"}

# Add
set.add("Element 4")
# Remove
list.remove("Element 3")
# Consult
is_in_list = "Element 1" in list


print(list) # ["Element 1", "Element 2"]
print(tuple) # ("Element 1", "Element 2", "Element 3")
print(set) # {"Element 1", "Element 4", "Element 2", "Element 3"}
print(is_in_list) # True