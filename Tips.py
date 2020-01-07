"""TIPS ON WRITING BETTER CODE IN PYTHON"""
"""NUMBER ONE
THE IDEA OF USING CONDITION IN THE IF ELSE CASES"""
condition = True
x = 1 if condition else 0
print(x)

"""NUMBER TWO
-THE IDEA OF USING UNDERSCORE WITH THE LARGE INTEGER VALUES"""

x = 1_000_000_000
y = 10_000_000
sum = x + y
print(f"{sum:,}")

""" ?  NUMBER THREE
THE IDEA OF INDEXING THE LISTS  i.e   ENUMERATION"""

names = ["nirajan", "narayan", "manoj", "nabaraj", "shanta"]
for index, name in enumerate(names, start=5):
    print(index, name)

"""number three
the idea  of using the zip function two loop through multiple lists at once
"""
names = ["nirajan", "narayan", "manoj", "nabaraj", "shanta"]
games_they_like = ["football", "basketball", "cricket", "pugb", "girls"]
for name, game in zip(names, games_they_like):
    print(f"{name} likes {game}.".title())

"""NUMBER FIVE
THE IDEA OF PRINTING REVERSE OF THE STRING"""
message = "cold silence has a tendency to atropy any sense of compassion"
print("reversed string= ", message[::-1])

"""NUMBER
THE IDEA OF zipping :D  THE TWO LISTS"""
numbers = [(1, 2, 3, 4, 5, 6), (7, 8, 9, 4, 5, 6)]
kerela = zip(*numbers)
print(kerela)
