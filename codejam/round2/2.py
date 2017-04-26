t=int(input())
for i in range(1,t+1):
 	[n,q]=input().split()
 	[n,q]=[int(n),int(q)]
 	ds=[]
 	ds.append([])
 	ds.append([])
 	for j in range(n):
 		[d,s]=input().split()
 		[d,s]=[int(d),int(s)]
 		ds[0].append(d)
 		ds[1].append(s)
 	route=[]
 	ans=[]
 	for j in range(n):
 		l=input().split()
 		for k in range(len(l)):
 			l[k]=float(l[k])
 		route.append(l)
 	
 	[u,v]=input().split()
 	[u,v]=[int(u),int(v)]	
 	minp=0	
 	for k in range(len(route[u])):
 		if (route[u][k]/ds[1][k])<minp and route[u][k]!=-1:
 			minp=route[u][k]/ds[1][k]
 			ks=k
 	ds[0][u]-=route[u][ks]
 	p1=u
 	u=ks

 	ans.append(minp)

 	minp=0
 	while u!=v:
 		for k in range(len(route[u])):
 			if route[u][k]/ds[1][k]<minp and route[u][k]!=-1:
 				minp=route[u][k]/ds[1][k]
 				k2=k

 		if 	ds[0][p1]>route[u][k2]:
 			if route[u][k2]/ds[1][p1]<minp:
 				ds[0][p1]-=route[u][k2]
 				minp=route[u][k2]/ds[1][p1]
 				ans.append(minp)
 				u=k2

 		else:
 			ans.append(minp)
 			u=k2
 			p1=k2
 	print("case %d: %f"%(t,ans))

 						
