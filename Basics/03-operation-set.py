set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

# Combine set_1 and set_2
print(set_1.union(set_2))  # {1, 2, 3, 4, 5, 6, 7}  A U B

# Find common elements in set_1 and set_2
print(set_1.intersection(set_2))  # {3, 4, 5}  A N B

# Find elements in set_1 which are not in set_2   A - B
print(set_1.difference(set_2))  # {1, 2}

print(set_1.symmetric_difference(set_2)) # {1, 2, 6, 7} (A U B) - (A N B)

####################################################

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

# Combine set_1 and set_2
print(set_1 | set_2)  # {1, 2, 3, 4, 5, 6, 7}

# Find common elements in set_1 and set_2
print(set_1 & set_2)  # {3, 4, 5}

# Find elements in set_1 which are not in set_2
print(set_1 - set_2)  # {1, 2}

###################################################

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
set_3 = {5, 6, 7, 8, 9}

# Combine set_1 and set_2 and set_3
print(set_1 | set_2 | set_3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}