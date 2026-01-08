
'''
# Simple hello world program with additional features
input_data = input("Name: ")
print(f"Hello, {input_data}!")

# Demonstrating type conversion
# Convert string numbers to integers and print the list 
print(list(map(int, ['1', '2', '3'])))

# Demonstrating basic conditional statements
# Check if a number is positive, negative, or zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")   

# Demonstrating string indexing
# Accessing individual characters in a string
name ="Harry"

print(name[0])  # Print the first character of the string
print(name[1])  # Print the second character of the string
print(name[2])  # Print the third character of the string
print(name[3])  # Print the fourth character of the string
print(name[4])  # Print the fifth character of the string   

# Demonstrating list indexing
# Accessing individual elements in a list
name = ["Harry", "Hermione", "Ron"]
print(name)
print(name[0])  # Print the first element of the list
print(name[1])  # Print the second element of the list
print(name[2])  # Print the third element of the list   

# Demonstrating tuple indexing
coordinates = (4, 5)
print(coordinates)
print(coordinates[0])  # Print the first element of the tuple
print(coordinates[1])  # Print the second element of the tuple


# Demonstrating list creation
names =["Harry", "Ron", "Hermione"]

names.append("Draco")  # Add "Draco" to the end of the list
names.sort()         # Sort the list in alphabetical order
print(names)


# Demonstrating set creation
s = set()

s.add(1)   # Add "Harry" to the set
s.add("Ron")     # Add "Ron" to the set
s.add("Hermione") # Add "Hermione" to the set

print(s)

# Demonstrating set removal
s.remove(1)
print(s)

# Demonstrating set length
print(f"Set has {len(s)} elements")


# Demonstrating for loop    
# Print double the value of each number in the list
for i in [1, 2, 3]:
    print(i * 2)

for i in range(3):
     print(i*2) 

name ="Harry Potter"
for char in name:
    print(char) 


# Demonstrating dictionary iteration
houses ={"Brendan": "Gryffindor", "Harry": "Gryffindor", "Draco": "Slytherin"}
for student in houses:
    print(f"{student} is in {houses[student]}") 

# Demonstrating dictionary modification
houses["Ziad"] ="Gryffindor"
print(houses["Ziad"])

'''
# Demonstrating function definition and usage
def square(num):
    return num * num    


for i in range(5):
    print(f"The square of {i} is {square(i)}")  