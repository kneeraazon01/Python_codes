# the function that can be treated as any other entities /objects
# i.e passed to function as an argument, assigned to a variable etc


def function(x):
    return x ** 2


# assigning a function to a variable
f = function
print(function)
print(f(5))

# passing function to another function as an argument


def cube(x):
    return x ** 3


cubes = []


def cube_mapped(fun, value):  # higher order function
    for i in value:
        cubes.append(fun(i))
    return cubes


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cube_mapped(cube, lists))


# RETURNING A FUNCTION FROM A FUNCTION
# LOOK AT IT...DEEKHO TOH SAHI
# bahut hard hei bhai ehh toh
def first_function(tag):
    def second_fun(msg):
        return "<{0}>{1}<{0}>".format(tag, msg)

    return second_fun


msg_1 = first_function("hi")
print(msg_1("this my friend is heading"))
