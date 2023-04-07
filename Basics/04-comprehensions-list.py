# Example 1
# First form

numbers = [1, 2, 3, 4, 5, 6]
multiply_numbers = []

for number in numbers:
    multiply_numbers = number * 10


# Second form

numbers2 = [1, 2, 3, 4, 5, 6]
multiply_numbers2 = [x * 10 for x in numbers2]

# Example 2

# First form

friends = ["Alberto", "Juan", "Pablo", "Isacc", "Israel"]
friends_starts_S = []

for friend in friends:
    if friend.startswith("I"):
        friends_starts_S.append(friend)

# Second form

friends = ["Alberto", "Juan", "Pablo", "Isacc", "Israel"]
friends_starts_S = [friend for friend in friends if friend.startswith("I")]
