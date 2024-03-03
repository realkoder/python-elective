# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = decorator(say_whee)


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

# ===================================================================

def callMyName(func):
    def wrapper():
        for i in range(0,2):
            print("MYNAMEE!!!")
            func()
    return wrapper

@callMyName
def something():
    print("HEY AFTER MY NAME")