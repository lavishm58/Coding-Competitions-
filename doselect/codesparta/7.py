b = int(input())
l=dict([('a',1), ('b',2), ('c',3),('x',24),('y',25),('z',26),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9),
        ('j',10),('k',11),('l',12),('m',13),('u',21),('v',22),('w',23),('n',14),('o',15),('p',16),
        ('q',17),('r',18),('s',19),('t',20)])
for i in range(b):
    we=input().split()
    we[0]=int(we[0])
    we[1]=int(we[1])
    mi=input().split()
    s=0
    for j in range(len(mi)):
        mi[j]=int(mi[j])
    x=input().split()
    
    a=None
    for j in range(len(x)):
        s=0
        for k in range(len(x[j])):
            s+=l[x[j][k]]*we[1]**mi[k]
        if j>0:    
            a+='+'+str(s)
        else:
            a=str(s)        
    print(a)        