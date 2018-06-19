
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def print_num(math_list):
    for item in math_list:
        print(item)

l = [add(2, 4), minus(6,3), multiply(3,5), divide(10,2)]

print_num(l)

