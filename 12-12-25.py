#Q1
a="python"
def reverse_string(a,i=0):
	if i == len(a)-1:
		return a[i]
	else:
		return reverse_string(a,i+1)+a[i]
print(reverse_string(a))


#Q2
a=19
b=91

sum1=0
while a:
	c=a%10
	sum1+=c
	a=a//10
sum2=0
while b:
	d=b%10
	sum2+=d
	b=b//10
if sum1 == sum2:
	print("True")
else:
	print("False")


#Q3
a=999
def one_digit(a):
	sum=0
	while a:
		b=a%10
		sum+=b
		a=a//10
	if sum > 9:
		a = sum
		return one_digit(a)
	else:
		return sum
print(one_digit(a))


#Q4
ListA= [4,4,4]
ListB= [1,2,3]
count=0
for i in range(len(ListA)):
	if ListA[i] > ListB[i]:
		count+=1
print(count)

#Q5
a="xyzxxy"
character = 'x'
b=[]
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if a[i] == character and a[j] == character:
			b.append(abs(i-j))
print(min(b))
