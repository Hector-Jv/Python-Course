students_age = {
    "Marco": 15,
    "Maria": 20,
    "Luis": 17,
    "Pedro": 18
}

# First form (incorrect)
for student in students_age:
    print(f'{student}: {students_age[student]}')

# Second form
for student, age in students_age.items():
    print(f'{student}: {age}')


#################
"""
students_age.values() return dict_values
sum return one value
"""
print(type(students_age.values()))
average_age = sum(students_age.values()) / len(students_age)
print(average_age)