a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
if a<=b and b<=c:
    print(a,b,c)
elif b<=a and a<=c:
    a,b=b,a
    print(a,b,c)
elif b<=c and c<=a:
    a,b,c=b,c,a
    print(a,b,c)
elif a<=c and c<=b:
    b,c=c,b
    print(a,b,c)
elif c<=a and a<=b:
    a,b,c=c,a,b
    print(a,b,c)
else:
    a,c=c,a
    print(a,b,c)