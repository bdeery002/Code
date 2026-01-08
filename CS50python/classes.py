
# Class in Python

#  This creates a new class named Point. A class is a blueprint for creating objects that can hold data and behavior.
# __init__ is a special method in Python called the initializer or constructor. It runs automatically when you create a new instance of the class.It takes three parameters:
#       self: refers to the instance being created.
#       x and y: values you pass when creating the Point object.
#  Inside the method:
#  self.x = x assigns the value of x to an attribute named x on the object.
#  self.y = y does the same for y
# If you create a point like this: p = Point(3, 4)
# Python calls __init__ with x=3 and y=4. The object p will have attributes p.x = 3 and p.y = 4


class Point():
    def __init__(self, x, y):
            self.x = x
            self.y = y

p = Point(3, 4)
print(f"Point coordinates are ({p.x}, {p.y})")  # Output: Point coordinates are (3, 4)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []   

    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        return True

    def open_seat(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
print(f"Flight capacity: {flight.capacity} and flight passengers: {flight.passengers}")  # Output: Flight capacity: 3

people = ["Alice", "Bob", "Charlie", "David"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")  