import datetime

def log_time(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        now = datetime.datetime.now()

        log_message = f"{now}: {func.__name__} was called with args: {args}, kwargs: {kwargs} and returned {result}\n"
        

        with open('log_function_time', 'a') as log_file:
            log_file.write(log_message)

        print(log_message)
        
        return result
    
    return wrapper


@log_time
def add(*args):
    return sum(args)

result = add(1,2,3)
print("Result", result)