n = int(input().strip())
a=['a','b','c','d','e','f','i','j','k','n','m','l','g',
		'h','o','p','q','r','s','t','u','v','w','x','z']
c=['b','c','d','f','j','k','n','m','l','g',
		'h','p','q','r','s','t','v','w','x','z']
v=['a','e','i','o','u']
c1=[]				
c2=[]
cc3=[]
cv3=[]
cc4=[]
cv4=[]
cc5=[]
cv5=[]
for i in range(len(c)):
	for j in range(len(v)):
		c1.append(c[i]+v[j])
		c2.append(v[j]+c[i])
if n==1:
	for i in range(len(a)):
		print(a[i])
elif n==2:
	for i in range(len(c)):
		for j in range(len(v)):
			print(c[i]+v[j])
			print(v[j]+c[i])

for i in range(len(c1)):
	for j in range(len(c)):
		cc3.append(c1[i]+c[j])
	for j in range(len(v)):
		cv3.append(c2[i]+v[j])
for i in range(len(cv3)):
	for j in range(len(c)):
		cc4.append(cv3[i]+c[j])
for i in range(len(cc3)):		
	for j in range(len(v)):
		cv4.append(cc3[i]+v[j])

for i in range(len(cv4)):
	for j in range(len(c)):
		cc5.append(cv4[i]+c[j])
for i in range(len(cc4)):		
	for j in range(len(v)):
		cv5.append(cc4[i]+v[j])

if n==3:	
	for i in range(len(c1)):
		for j in range(len(c)):
			print(c1[i]+c[j])
		for j in range(len(v)):
			print(c2[i]+v[j])	
if n==4:
	for i in range(len(cv3)):
		for j in range(len(c)):
			print(cv3[i]+c[j])
	for i in range(len(cc3)):		
		for j in range(len(v)):
			print(cc3[i]+v[j])	
if n==5:
	for i in range(len(cv4)):
		for j in range(len(c)):
			print(cv4[i]+c[j])
	for i in range(len(cc4)):		
		for j in range(len(v)):
			print(cc4[i]+v[j])					
if n==6:
	for i in range(len(cv5)):
		for j in range(len(c)):
			print(cv5[i]+c[j])
	for i in range(len(cc5)):		
		for j in range(len(v)):
			print(cc5[i]+v[j])
