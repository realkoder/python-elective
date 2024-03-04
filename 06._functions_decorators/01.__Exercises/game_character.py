
def add_comma_space(func):
    def wrapper():
        return "".join([func(), ", "])
    return wrapper

def add_and_space(func):
    def wrapper():
        return "".join([func(), " and "])
    return wrapper

def add_punctum(func):
    def wrapper():
        return "".join([func(), "."])
    return wrapper

def sharpshooter(func):
    def wrapper():
        return "".join([func(), "the sharpshooter"])

    return wrapper

def stealthy(func):
    def wrapper(): 
        return "".join([func(), "stealthy character"])
    return wrapper


@add_punctum
@stealthy
@add_and_space
@sharpshooter
@add_comma_space
def player():
    return "I'm the player character"

print(player())

player = stealthy(player)
