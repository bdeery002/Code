# Define a decorator function called 'announce' that takes a function 'f' as an argument
def announce(f):
    def wrapper():
        print("About to run the function...")
        result = f()
        print("Function has completed.")
        return result
    return wrapper

# Use the decorator on a simple function 'hello' that prints "Hello, world!"
@announce
def hello():
    print("Hello, world!")

# Call the decorated function
hello()