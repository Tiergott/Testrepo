def song(st=3,l=3,p=0):
    try:
        st=int(st)
    except:
        print("First entered value is not a number")
    w="la-"*int(l)
    if st == 0:
        print("There is no strings in your song")
        exit()
    if l == 0:
        print("There is no words in your song")
        exit()
    strings=str(w.rstrip("-")+"\n")*(int(st)-1)+ w.rstrip("-")
    if p==0:
        strings=strings+"."
        return strings
    elif p==1:
        strings=strings+"!"
        return strings
    else:
        print("Third value in function is not 0 or 1. Please, enter correct value")
        exit()

print(song(2,3,0))




