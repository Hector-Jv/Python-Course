# Example 1
# First form
def add(x, y):
    return x + y

# Second form
add = lambda x, y: x + y

# Example 2

numbers = [1, 2, 3, 4]
doubled = [(lambda x: x*2)(x) for x in numbers ] # confusied
doubled = list(map(lambda x: x*2, numbers))

print(type(map(lambda x: x*2, numbers))) # type map
