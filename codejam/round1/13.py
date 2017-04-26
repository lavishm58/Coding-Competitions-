import math
t=int(input())
			
def split(p,r,a):
	if p<r-1:
		q=int((p+r)/2)
		a.append(q)
		split(p,q,a)
		split(q+1,r,a)
	return a	


for i in range(t):
	[n,k]=input().split()
	[n,k]=[int(n),int(k)]
	p=[]
	if n%2==1:
		p1=(int(n/2)+1)
	else:
		p1=(n/2)

	a=[]
	a=split(1,n,a)
	print(a)	