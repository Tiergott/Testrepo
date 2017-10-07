def sec_big(*args):
    l=list(args)
    l.sort()
    if l.count(l[1]) > 1:
        return l[l.count(l[1])]
    else:
        return l[1]

#print(sec_big(1.01,2.01,2.01,2.01,3.01,2,3.01,2.01,5.01,2.01))
print(sec_big("a","b","c","ann","bob","a","b","b","john","ann"))