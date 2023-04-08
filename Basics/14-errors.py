def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

grades = []

# First mode

try:
    average = divide(sum(grades), len(grades))
    print(f'The average grade is {average}.')
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")

# Seconde mode

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
# except ValueError:
    # Code
else:
    print(f'The average grade is {average}.')
finally:
    print("Correct and incorrect result, this line is execute")

