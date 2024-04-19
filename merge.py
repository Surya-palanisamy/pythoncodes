
def merge(a,b):
    c = []
    while len(a)!=0 and len(b)!=0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else :
            c.append(b[0])
            b.remove(b[0])
    if len(a)==0:
        c +=b
    else:
        c+=a
    return c
def mergesort(v):
    if len(v) ==0 or len(v) == 1:
        return v
    else :
        mid = len(v)//2
        a= mergesort(v[:mid])
        b=mergesort(v[mid:])
    return merge(a,b)
s = [89,1,23,56,34,76,7,5,2]
print(mergesort(s))


