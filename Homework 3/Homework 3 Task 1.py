a = input("Enter a string with minimum of 5 symbols:")
try:
    a[4]
except:
    print('Length of entered string is less, than 5 symbols')
    exit()
print(a[2],a[-2],a[0:5],a[0:-2],a[::2],a[1::2],a[::-1],a[::-2],len(a),sep='\n')