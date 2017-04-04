t=int(input())
class a:
	def __init__(self,n,m,i,j):
		self.n=n
		self.m=m
		self.i=i
		self.j=j
	def left(self):
		self.j=self.j-1
	def right(self):
		self.j=self.j+1
	def up(self):
		self.i=self.i-1
	def down(self):
		self.i=self.i+1	
b=a(1,1,1,1)
count=0
for i in range(t):
	n,m=input().split()
	[n,m]=[int(n),int(m)]
	s=input()
	r=[0]*n
	s=[0]*m
	r=[j for j in range(1,n+1)]
	s=[j for j in range(1,m+1)]
	p=[]
	for k in r:
		for j in range(m):
			p.append((k,s[j])) 
	for k in p:
		b=a(n,m,i,j)
		i=k[0]
		j=k[1]
		q=0
		for x in s:
			if b.i!=1 and b.j!=1: 
				if x=='L':
					b.left()
					if b.j>m or b.j<=0:
						break
				elif x=='R':
					b.right()
					if b.j<=0 or b.j>m:
					
						break
				elif x=='U'and b.up().i+b.j<=(n+m):
					b.up()
					if b.i>n or b.i<=0:
						break
				elif x=='D'and b.down().i+b.j<=(n+m):
					b.down()
					if b.i>n or b.i<=0:
						break
			if (b.i==1 or b.j==1) and q!=len(s):
				break
			q=q+1	
		if q==len(s):
			count+=1
	if count==0:
		print('unsafe')
	else:
		print('safe')		
