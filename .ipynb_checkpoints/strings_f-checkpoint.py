message = "Joey : How you doin'?"

# this is the most general of all
# ! fancier comment, better comment, jaja :D
# ? this one is new
# todo this one is different looks good too  and  is helpful at the same time

# slicing strings
print(message[0:8])
print(message[::-1])  # reverses the string
            
# builtin methods on strings

print(len(message))
print(message.count("namaste"))
print(message.upper())
print(message.title())

# string concatination

greeting = "Hello"
name = "Nirajan"
print(greeting.title(), " ", name)


# # the same thing on formating with placeholders and displaying
greeting = "Hello"
name = "Nirajan"
# print(greeting + name)  # mistake
# print(greeting + ", ", name)
message = "%s, %s. Welcome!" % (greeting, name)  # using the place holders
messagee = "{}, {}. Welcome!".format(greeting, name)  # using the string formatting
print(
    f"{greeting}, {name.upper()}. welcome!"  # isn't this amazingly short yet much useful
)  # Let's cosider it to be the most advanced string formatting  ?
print(message)
print(messagee)


# find help

methods = dir(message)
for method in methods:
    print(method)

print(help(str))
print(help(str.upper))


message = "hELLLLllo There, how you doin?"
print(message.lower().capitalize())
methods = dir(message)
for method in methods:
    print(method)

print(help(str.capitalize))
print(help(str.upper))

