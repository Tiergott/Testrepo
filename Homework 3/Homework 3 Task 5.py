def is_leap_year(y):
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        return True
    else:
        return False

def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# print(is_leap_year(405))

# print(triangle(8,3,4))

