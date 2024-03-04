
def sharpshooter(func):
    def wrapper():
        return "".join([func(), ", the sharpshooter"])

    return wrapper

def stealthy(func):
    def wrapper(): 
        return "".join([func(), " and stealthy character."])
    return wrapper

@stealthy
@sharpshooter
def player():
    return "I'm the player character"

print(player())

player = stealthy(player)
