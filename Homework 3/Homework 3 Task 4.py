#First part of task


l=[23,12,0,98,76.5,82,1.1]
print(l)
while l:
    print(l.pop(0))
print(l)


#Second part of task


s="Automation"
print(s)
while s:
    print(s[0])
    s=s.replace(s[0], '')
print(s)


#Third part of task


m=[23,12,0,98,76.5,82,1.1]
print(m)
while m:
    m.sort()
    print(m.pop(0))
print(m)

#Fourth part of task

a='Quote: "We are not what we should be! \nWe are not what we need to be. \nBut at least we are not what we used to bе \n(Football, volleyball Coach)"'
lst=[]
dct={}
print(a)
print(len(a.split()))
for i in range(len(a.split())):
    sp=((((((a.split()[i].strip('!')).strip('.')).strip(',')).strip(':')).strip('"')).strip(')')).strip('(')
    sp=sp.lower()
    lst.append(sp)
def word_count():
    for i in lst:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
lst.sort()
print(lst)
word_count()
for i in dct:
    print(i,dct[i])