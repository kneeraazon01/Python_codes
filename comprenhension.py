nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for i in nums:
    my_list.append(i)
    print(my_list)

# ? my_list=[x for x in nums]
# print(my_list)

my_list = [n * n for n in nums]
print(my_list)

# using maps and lambdang maps and lambda
my_list = map(lambda n: n * n, nums)
k = print(my_list)
# now to select the even ones only form the list

# my_list=[n**2 for n in nums if n%2==0]
# print(my_list)

my_list = filter(lambda n: n % 2 == 0, nums)

print(list(my_list))

my_list = []
for letter in "abcd":
    for num in range(4):
        my_list.append((letter, num))
        print(my_list)


my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)


# AND NOT TO DICTIONARIES


names = ["nirajan", "karina", "manisha", "sangita"]
for index, name in enumerate(names):
    print(index, name)

    names = ["nirajan", "manoj", "narayan", "shanta"]
    superheroes = ["iron man", "deadpool", "antman", "root"]
# my_dict={}
# for name,superpower in zip(names,superheroes):
#     my_dict[name]=superpower
# print(my_dict)
my_dict = {
    name: superpower
    for name, superpower in zip(names, superheroes)
    if name != "nirajan"
}
print(my_dict)

numbers = [1, 2, 3, 1, 2, 5, 4, 6, 7, 8, 9, 5, 4, 2, 3, 6, 5, 4, 1, 7, 9]
my_set = set()
for num in numbers:
    my_set.add(num)
    print(my_set)

    my_set = {n for n in numbers}
    print(my_set)

# def fun(numbers):
#     for n in numbers:
#         yield n*n
# number=fun(numbers)
# print(list(number))

nums = (n * n for n in numbers)
for i in nums:
    my_gen = i
    print(my_gen)
    for i in range(10):
        print("nothing")
