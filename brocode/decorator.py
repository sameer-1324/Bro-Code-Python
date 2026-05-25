# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper():
        print("add sprinkles")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("add fudge")
        func()
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()