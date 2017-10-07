def triangle_type(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        if a==b and b==c:
            return "Equilateral triangle"
        elif a==b or b==c or a==c:
            return "Isosceles triangle"
        elif a!=b and b!=c:
            return "Versatile triangle"
    else:
        return "Not a triangle"

print(triangle_type(4,4,4))