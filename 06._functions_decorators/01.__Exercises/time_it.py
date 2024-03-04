import time

def time_a_func(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@time_a_func
def print_string():
    print("Jeg printer noget nu man!")

print_string()