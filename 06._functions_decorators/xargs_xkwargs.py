
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += " " + arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# ============================================= Unpacking operator
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)

# Above prints following
# 1
# [2, 3, 4, 5]
# 6