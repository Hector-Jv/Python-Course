class Student:
    def __init__(self, name):
        self.nombre = name
        self.grades = (8, 10, 9)

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"This is a student {self.nombre}"

student = Student("Israel")
print(student.average_grades())


# Excercise

class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {
            "name": name,
            "price": price
        }
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # sum([item["price"] for item in self.items])
        return sum(list(map(lambda x: x["price"], self.items)))