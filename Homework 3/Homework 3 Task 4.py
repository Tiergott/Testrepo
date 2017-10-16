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
    # s=s.replace(s[0], '')
    s=s[1:]
print(s)


#Third part of task


m=[23,12,0,98,76.5,82,1.1]
print(m)
m.sort()
while m:
    print(m.pop(0))
print(m)

#Fourth part of task

a='Quote: "We are not what we should be! \nWe are not what we need to be. \nBut at least we are not what we used to bе \n(Football, volleyball Coach)"'
lst=[]
n=a.split()
print(a)
print(len(n))
for i in range(len(n)):
    sp=n[i].strip("[,.:;!\"\')(]")
    sp=sp.lower()
    lst.append(sp)
lst.sort()
def word_count(nlst):
    dct={}
    for i in nlst:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
    print(dct)
def word_similar(mlst):
    t = []
    for i in mlst:
        if i not in t:
            t.append(i)
    print(t)
print(lst)
word_similar(lst)
word_count(lst)