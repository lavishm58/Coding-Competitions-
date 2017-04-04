import math
import itertools 

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
xi=[None]*n
wi=[None]*n
for i in range(n):
    x,w = input().strip().split(' ')
    xi[i],wi[i] = [int(x),int(w)]
xi.reverse()
wi.reverse()
ki=[]
sum=[0]
p=0
j=0
if k!=1:
	for a in itertools.combinations(xi[0:n-1],k-1):
		a=[a]
		a=[list(item) for item in a]
		a=a[0]
		for i in range(len(xi)):
			if xi[i]>max(a):
				sum[j]+=wi[i]*(xi[i]-max(a))
			if xi[i]==max(a) and len(a)!=1:
				a.remove(max(a))
			if xi[i]<max(a) and len(a)==1:
				sum[j]+=wi[i]*(xi[i]-xi[len(xi)-1])
		j+=1
		sum.append(0)
	print(min(sum[:-1]))	

else:
	for i in range(len(xi)):
		p+=wi[i]*(xi[i]-xi[len(xi)-1])
	print(p)
