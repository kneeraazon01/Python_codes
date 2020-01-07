# lists
courses = ["maths", "science", "history", "arts"]
print(courses)

print(len(courses))

# SLICING THE LIST WORKS SAME WAY AS THE STRINGS


print(courses[1])

print(courses[-1])

print(courses[::-1])
# print(courses[5]) #ERROR out of index

for index, item in enumerate(courses, start=2):
    print(index, item)

updated_list = []
courses = ["maths", "science", "history", "arts"]
courses.append("computer")
print(updated_list)
print(courses)

courses.insert(1, "chemistry")
print(courses)

courses_2 = ["law", "education"]
courses.insert(0, courses_2)
print(courses)
courses.extend(courses_2)
print(courses)
courses.remove("maths")
print(courses)
popped = courses.pop()
print(courses, "\n", popped)
courses.reverse()
print(courses)
# courses.sort()
print(courses)
num = [1, 5, 4, 6, 7, 8, 9, 5, 4, 5, 6, 7]
num.sort()
print(num)
courses = ["maths", "science", "history", "arts"]
sorted_list = sorted(courses)
print(sorted_list)
print(courses.index("arts"))

num = [1, 5, 4, 6, 7, 8, 9, 5, 4, 5, 6, 7]
print(max(num))
print(min(num))


print(8 in num, 10 in num)


courses = ["maths", "science", "history", "arts"]
print("----".join(courses))
splitted_list = str(courses).split(".")
print(splitted_list)
