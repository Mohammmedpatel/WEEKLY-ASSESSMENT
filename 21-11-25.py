a={
    "user": {
        "firstname": "Alice",
        "lastname": "Brown"
    },
    "age": 30
}
d={}
c=""
def flat_dict(a):
	global d,c
	for i in a:
		if isinstance(a[i],dict):
			c+=i+"."
			flat_dict(a[i])
		else:
			d[f"{c}{i}"]=a[i]
flat_dict(a)
print(d)

b=[3, 1, 3, 2, 2, 4]
c=[]
for i in b:
	if i not in c:
		c.append(i)
print(c)

a=[1, 5, 2, 5, 3]
for i in range(len(a)):
	if a[i] in a[i+1:]:
		print(a[i])
		break


a="Code is fun"
b=[]
c=""
for i in a:
	if i != " ":
		c+=i
	else:
		b.append(c)
		c=""
c+=i
b.append(c)
print(len(b))
	
a={'m': 22, 'n': 10, 'o': 35, 'p': 18}
c={}
b=list(sorted(a.values()))
d=['n','p','m','o']
print(b)
for i in b:
	if i not in c:
		c[i]=d[i]
print(c)
	