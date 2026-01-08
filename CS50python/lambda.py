# Demonstration of lambda functions in Python. A lambda function is a small anonymous function defined with the lambda keyword. 
# It can take any number of arguments but can only have one expression.   

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


people.sort(key=lambda person: person["age"])  # Sorts the list of people by age using a lambda function as the key
print(people)
