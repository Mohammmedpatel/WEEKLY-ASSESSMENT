a="apple banana mango".split()
b="banana orange apple".split()
c=[]
for i in a:
	if i in b:
		c.append(i)
print(c)


a=[1, 2, 3, 4, 6]
K = 6
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if a[i]*a[j]==K:
			print((a[i],a[j]))


d=[4, 7, 10, 12]
target = 9
b=[]
for i in d:
	b.append(abs(target-i))
c=b.index(min(b))
print(d[c]) 


a=["interview", "internet", "internal"]
b=len(max(a,key=len))
c=""
for i in range(b):
	if a[0][i]==a[-1][i]:
		c+=a[0][i]
	else:
		break
print(c)

a="aeiou"
a=a.lower()
c="aeiou"
b=[i for i in a if i in c]
d=-1
e=""
for j in a:
	if j in c:
		e+=b[d]
		d+=-1
	else:
		e+=j
print(e)