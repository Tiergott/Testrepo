a = input("Enter a string:")
if len(a)%2 == 0:
    s=a[(len(a)//2):]+a[:(len(a)//2)]
    print(s)
else:
    s=a[(len(a)+1)//2:]+a[:(len(a)+1)//2]
    print(s)