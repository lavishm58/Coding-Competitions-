n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
a = list(map(int, input().strip().split(' ')))
print(a)
for i in range(q):
    left,right,x,y = input().strip().split(' ')
    left,right,x,y = [int(left),int(right),int(x),int(y)]
    count=0
    for j in range(len(a)):
    	if left<=j<=right and a[j]%x==y:
    		count+=1
    print(count)		
