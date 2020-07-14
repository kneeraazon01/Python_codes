# ? class basics
#  ! better comments ! creating and instances of the class
# ? todo classes are used in the programming to group of similar data
#  todo to use and then reuse in the other places in future
# to make programming easier
#  you know that
# so let's get started

# data and functions = attributes-> of a class
# method = functions within the classes

# FIRST WAY


class employeee:
    pass

    def __init__(self, first, last, pay):
        self.first = first
        self.second = last
        self.pay = pay
        self.email = (last + "" + first + "@company.com").lower()


emp_1 = employeee("Nirajan", "karki", 50000)
print(emp_1.first)
print(emp_1.email)

#! SECOND WAY


class employee:
    def __init__(self, name, lastname, pay):
        self.fisrt = name
        self.last = lastname
        self.pay = pay
        self.email = (lastname + "" + name + "@company.com").lower()

    def fullname(self):
        return ("{} {}".format(self.fisrt, self.last)).title()


emp_1 = employee("nirajan", "karki", 50000)
print(emp_1.fullname())
print(emp_1.email)
print(emp_1.pay)



look at this s s fsdfsdfsdfsdfsdfefs