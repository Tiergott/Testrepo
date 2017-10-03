n=int(input("Enter year:"))
if n%4 == 0 and n%100 != 0:
    print("YES")
elif n%400 == 0:
    print("YES")
else:
    print("NO")