# nice, we can document the functions and <strong> works just like in other languages!

def is_leap_year(year : int):
    """
    Returns whether the given <strong>year</strong> is leap or not

    :param year: 
    :type year: int
    :return type: boolean
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# documentation can be read
print(is_leap_year.__doc__)
# it can be written too! Though it's just a silly test here, ofc no one dares touch __Keys in production
is_leap_year.__doc__ = "Hello World!"
print(is_leap_year.__doc__)