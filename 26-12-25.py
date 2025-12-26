#Q1
from functools import reduce
a=[1,0,3,4]
li=[]
for i in range(len(a)):
	li.append(reduce(lambda x,y:x*y,a[:i]+a[i+1:]))
print(li)


#Q2
employees = {
"A": 1000,
"B": 2000,
"C": 3000,
"D": 4000,
"E": 5000
}
li1=[]
sorted_salary = sorted(employees,key=employees.get,reverse=True)
#print(sorted_salary)
for i in sorted_salary:
	if len(li1) != 3:
		li1.append((i,employees[i]))
print(li1)	


#Q3
from collections import Counter
attendance = {
"Monday": ["Ahmed", "Fatima", "Hassan"],
"Tuesday": ["Fatima", "Ali", "Zainab"],
"Wednesday": ["Ahmed", "Hassan", "Ayesha"],
"Thursday": ["Fatima", "Ali", "Hassan"],
"Friday": ["Ahmed", "Fatima", "Zainab", "Ayesha"]
}
li3=[]
for i in attendance:
	li3.extend(attendance[i])
#print(li3)
a = Counter(li3)
b=max(a,key=a.get)

print(b,a[b])


#Q4
students = [
{"name": "Ahmed", "marks": [85, 90, 78]},
{"name": "Fatima", "marks": [92, 88, 95]},
{"name": "Hassan", "marks": [65, 70, 68]},
{"name": "Ayesha", "marks": [88, 85, 90]}
]

def avg_calculation(marks_list):
  stu_avg = sum(marks_list["marks"])/len(marks_list["marks"])
  marks_list["average"]=stu_avg
  return marks_list

stu_avg=list(map(avg_calculation,students))
print(list(filter(lambda x:x["average"]>=80,stu_avg)))



#Q5
a=[7,8,9,11,12]
for i in range(1,len(a)+2):
	if i not in a:
		print(f"{i} is missing")
		break
else:
	print(i)

	






























































































