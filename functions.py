# FUNCTIONS

# 
def hellofunc():
    return "Say my name:"


for i in range(100):
    print(hellofunc())


def hello(greeting, name="Nirajan"):
    return "{} {} ".format(greeting, name)


print(hello("Hi"))

# NOW THIS PART IS IMPORTANT


def info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["maths", "arts", "science"]
information = {"name": "Nirajan", "lastname": "Karki", "age": 2}
info(*courses, **information)


# LEAP YEAR
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):

    # return   true for leap years and not true i.e false for not leap years
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    # return days  in month for that year
    if not 1 < month <= 12:
        return "invalid month"
    elif month == 2 and is_leap_year(year):
        return 29
    return month_days[month]


print(is_leap_year(2003), days_in_month(2004, 2))

