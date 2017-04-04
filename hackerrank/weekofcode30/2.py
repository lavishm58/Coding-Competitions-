import itertools
ki=[]
t=int(input())
for i in range(t):
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	nos=input().split()
	for j in range(len(nos)):
		nos[j]=int(nos[j])
	for L in range(0, len(nos)+1):
		for a in itertools.combinations(nos,L):
			if len(a)>=2:
				ki.append(a)			
	b=[]
	count=[0]*len(ki)
	for j in range(len(ki)):
		for a in itertools.combinations(ki[j],2):
			if sum(a)%k==0:
				count[j]+=1
	d=[]
	for j in range(len(count)):
		if count[j]==min(count):
			d.append(len(ki[j]))
	print(max(d))			



