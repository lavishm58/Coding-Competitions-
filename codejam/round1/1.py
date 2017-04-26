file=open("A-large-practice.in",'r')
t=int(file.readline())
out=open("out.txt",'w')

for i in range(1,t+1):
	num=int(file.readline())
	j=1
	q=[]
	while True:
		s=str(j*num)
		
		for d in str(s):
			if int(d) not in q:
				q.append(int(d))
		q.sort()		
		if q.__eq__([0,1,2,3,4,5,6,7,8,9]):
			break		
		if j>1000:
			out.write('Case #%d: INSOMNIA\n'%i)
			break	
		j+=1
	if j<1000:	
		out.write('Case #%d: %d\n'%(i,j*num))	
				

file.close()				
out.close()
