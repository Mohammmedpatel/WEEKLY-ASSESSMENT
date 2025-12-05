#Q1
a=[2, 4, 7, 8]
b=[]
for i in a:
	if i%3==0 or i%5==0:
		b.append(i)
print(len(b))


#Q2
a="Python is fun".split()
b=""
for i in range(len(a)-1,-1,-1):
	b+=a[i]+" "
print(b)


#Q3
a="cat"
b="bat"
for i in a:
	if i not in b:
		print("FALSE")
		break
else:
	print("TRUE")


#Q4
n=5
for i in range(n):
	for j in range(n):
		if i == j:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()	

		
#Q5
a="level noon civic".split()
b=[]
for i in a:
	if i == i[::-1]:
		b.append(i)
else:
	print("")
		
if b:
	print(max(b,key=len))