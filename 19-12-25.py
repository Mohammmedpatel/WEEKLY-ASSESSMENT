#Q1
String = "leetcode"
Dict = ["leet", "code", "leetcode"]
if String in Dict:
	print("True")
else:
	print("False")


#Q2
Coins = [1, 2, 5]
Amount = 9
lst =[]
count=0
for i in Coins:
	if i % Amount == 0:
		count = Amount // i
		lst.append(count)
	
		
else:
	 print("-1")
print(lst)


#Q3
a="abcabcbb"  
b=""
c=[]
for i in a:
	if i not in b:
		b+=i
	else:
		c.append(b)
		b = ""
print(len(max(c,key=len)))


#Q4
a="4[xy]5[y]"
li=[]
str1=""
for i in range(len(a)):
  if a[i] == "[":
    j = i+1
    while a[j] != "]":
      str1+=a[j]
      j+=1
    li.append(str1)
    str1=""
print(li)


z=0
str2=""
for k in a:
  if k.isdigit():
    str2+=int(k)*li[z]
    z+=1
print(str2)


#Q5
str1="hello,,,world,,python,"
lst1=[]
c=""
for i in str1:
	if i != ",":
		c+=i
	else:
		lst1.append(c)
		c=""
if c:
	lst1.append(c)

lst2=[]
for j in lst1:
	if j != "":
		lst2.append(j)
print(",".join(lst2))		
