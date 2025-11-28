#a=["race", "care", "note", "tone", "state", "taste", "abc", "bca"]
#d={}
#for i in a:
#	d["".join(sorted(i))]=d.get(i,[])+[i]
#print(list(d))


d1 = {'x': 10, 'y': 20, 'z': 30}
d2 = {'y': 15, 'z': 45, 'w': 50}

for i in d2:
	if i in d1:
		d1[i]=d2[i]+d1[i]
	else:
		d1[i]=d2[i]
print(d1)

#a={'u': 12, 'v': 5, 'w': 25, 'x': 7}
#b=[]
#for i in a:
#	b.append(i[a])
#b.sort()
	
