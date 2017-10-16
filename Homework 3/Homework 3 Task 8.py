def song(st=3,l=3,p=0):
    assert st == int(st), "First entered value is not an integer number"
    assert l == int(l), "Second entered value is not an integer number"
    assert st != 0, "There is no strings in your song"
    assert l != 0, "There is no words in your song"
    w = "la-"*int(l)
    strings=str(w.rstrip("-")+"\n")*(int(st)-1)+ w.rstrip("-")
    if p==0:
        strings+="."
        return strings
    elif p==1:
        strings+="!"
        return strings
    else:
        print("Third value in function is not 0 or 1. Please, enter correct value")
        return

print(song(7,2,1))




