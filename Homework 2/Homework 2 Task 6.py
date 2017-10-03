a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a == b and b == c:
    print(3)
elif a == b and b != c or b == c and a != c or a == c and b != c:
    print(2)
else:
    print(0)