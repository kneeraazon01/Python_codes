import random

a = input()
a_2 = a
list = []
dic = {}
final_dic = {}
display = ""
n = 0
length = len(a)
for i in range(15):
    random_number = 10 * random.random()
    random_number = str(random_number)
    number = random_number[0]
    number = int(number)
    if number < length:
        a = a.replace(a[number], "_")
print(a)
for i in a:
    list.append(i)
print(list)
for i in a_2:
    dic = {i: n}
    final_dic.update(dic)
    n += 1
while True:
    ans = input()
    if ans in a_2:
        no = final_dic[ans]
        list.remove(list[no])
        list.insert(no, ans)
        print(list)
    for i in list:
        display += i
    print(display)
    if display == a_2:
        break
    display = ""

