#Q1
lst1 = [3,1,2,4,7,6]
odd = []
even = []
for i in lst1:
	if i%2 == 0:
		even.append(i)
	else:
		odd.append(i)
print(odd+even)

#Q2
lst2 = [16,17,4,3,5,2]
result = []
for i in range(len(lst2)):
	a = lst2[i]
	for j in range(i+1,len(lst2)):
		if a < lst2[j]:	
			break
	result.append(a)

print(result)


#Q4
lst4 = [-1,2,-3,4,-5,6]
pos = []
neg = []
for num in lst4:
	if num >= 0:
		pos.append(num)
	else:
		neg.append(num)
result = []
i = j = 0
while i < len(neg) and j < len(pos):
	result.append(neg[i])
	result.append(pos[i])
	i+=1
	j+=1
result.extend(neg[i:])
result.extend(pos[i:])

print(result)


#Q5
lst3 = [1,3,5,2,2]
result=[]
for i in range(len(lst3)):
	if sum(lst3[:i]) == sum(lst3[i+1:]):
		result.append(i)
print(result)
		