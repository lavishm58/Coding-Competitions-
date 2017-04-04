
# Read the variable from STDIN
nq = input().split()
st=input()
p=[0]*len(st)
for i in range(int(nq[1])):
    x=input().split()
    count=0
    if len(x)==2:
        for i in st:
            if i==x[1]:
                if p[i]==0:
                    p[i]=1
                else:
                    p[i]=0
    else:
        l=int(x[1])
        r=int(x[2])
        for i in range(l-1,r):
            if x[3]=='off':
                if p[i]==0:
                    count+=1
            else:
                if p[i]==1:
                    count+=1
        print(count)            
            
            
# Output the variable to STDOUT
