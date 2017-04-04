n=int(input().strip())
a='min(int, int)'
if n==2:
	print('min(int, int)')
	
else:
	for i in range(n-2):
		a='min(int, '+a+')'
	print(a)	