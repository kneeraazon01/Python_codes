import os
import sys
import math

print(sys.version)
sets = {"maths", "science", "history", "arts"}
sets_1 = {"maths", "design", "history", "arts"}
# print("maths" in sets)
intersect = sets.intersection(sets_1)
print(intersect)
unions = sets.union(sets_1)
print(unions)


# empty lists tuples and sets
empty_list = []
# or
empty_list = list()

empty_tuple = ()
# or
empty_tuple = tuple()

# empty_set={} doens't work because it's not the set its a dictionary
# but it works this way only
empty_set = set()
