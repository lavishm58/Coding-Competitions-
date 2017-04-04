t=int(input())
for i in range(t):
	n=int(input())
	h=input().split()
	for j in range(len(h)):
		h[j]=int(h[j])
	count=0	
	ans=count
	count=1
	h.sort()
	for j in range(len(h)-1):
		if h[j]==h[j+1]:
			count+=1
		
		else:
			ans=count*(count-1)
			count=1
	if count!=1:
		ans=count*(count-1)						

	print(ans)				