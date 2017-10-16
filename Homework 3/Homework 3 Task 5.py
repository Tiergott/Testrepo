def is_leap_year(y):
    assert type(y) != str, "Year can not be string"
    assert y == int(y), "Year can not be not integer number"
    assert y > 0, "Year can not be 0 or less than 0"
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        return True
    else:
        return False

def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# print(is_leap_year(2012))

# print(triangle(8,3,4))

