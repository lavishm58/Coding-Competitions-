nt=input().strip().split(' ')
for i in range(len(nt)):
	nt[i]=int(nt[i])
c=list(map(int, input().strip().split(' ')))
t=nt[1]
n=nt[0]
full=n
new=0
for i in range(t):
	if i!=t-1:
		n=n-c[i]
		if n<5:
			new+=full-n
			n=full
		else:
			n=n		
print(new)			