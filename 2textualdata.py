message = "What on the world is going on Doctor?, Is it all going to be alright again?"

print(message)
print(message.upper())
print(message.title())
replaced_message = message.replace("Doctor", "Don Corleone")
print(replaced_message)


print(
    message.find("going")
)  # tells us the starting index of passed argument, in here going==21
# and if not found the argument passed in it simply returns the value==-1
print(len(message))


print(message.count("on"))
print(message[4:25])
# print(message[140])  # will throw an ouot of index error


messages = message.split(" ")
# print(message, end="?")
for item in messages:
    print(item)
print(messages)
