# FOR LOOP
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    if num == 8:
        print("found!")
        continue
    print(num)


for i in range(1, 2, 10):
    print(i)


# NESTED LOOP

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    for letter in "abc":
        print(num, letter)

# RANGE

for i in range(1, 20, 2):
    print(i)

# WHILE LOOP

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
