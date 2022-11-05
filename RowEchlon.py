print("Apurva Shaw DS Assignment")
import numpy as np
list1 = []
list2 = []
list3 = []
list4 = []

for x in range(4):
    a = int(input("Enter the numbers:"))
    list1.append(a)

for x in range(4):
    a = int(input("Enter the numbers:"))
    list2.append(a)

for x in range(4):
    a = int(input("Enter the numbers:"))
    list3.append(a)
for x in range(4):
    a = int(input("Enter the numbers:"))
    list4.append(a)
   

matrix = np.array([list1,list2,list3,list4])
print(matrix)

arr=[]
for i in range (4):
    arr.append((matrix[0][i])/matrix[0][0])
print("\n")


for i in range (4):
    arr[i]=arr[i]*matrix[3][0]


for i in range (4):
    matrix[3][i]=matrix[3][i]-arr[i]
print(matrix)

#--------------------------
arr1=[]
for i in range (4):
    arr1.append((matrix[0][i])/matrix[0][0])
print("\n")


for i in range (4):
    arr1[i]=arr1[i]*matrix[2][0]


for i in range (4):
    matrix[2][i]=matrix[2][i]-arr1[i]
print(matrix)

#--------------------------
arr2=[]
for i in range (4):
    arr2.append((matrix[0][i])/matrix[0][0])
print("\n")


for i in range (4):
    arr2[i]=arr2[i]*matrix[1][0]


for i in range (4):
    matrix[1][i]=matrix[1][i]-arr2[i]
print(matrix)


#--------for second column------------------
arr3=[]
for i in range (4):
    arr3.append((matrix[1][i])/matrix[1][1])
print("\n")

for i in range (4):
    arr3[i]=arr3[i]*matrix[3][1]


for i in range (4):
    matrix[3][i]=matrix[3][i]-arr3[i]
print(matrix)
#-------------------------------------
arr4=[]
for i in range (4):
    arr4.append((matrix[1][i])/matrix[1][1])
print("\n")


for i in range (4):
    arr4[i]=arr4[i]*matrix[2][1]


for i in range (4):
    matrix[2][i]=matrix[2][i]-arr4[i]
print(matrix)

#-------------for column 3------------
arr5=[]
for i in range (4):
    arr5.append((matrix[2][i])/matrix[2][2])
print("\n")


for i in range (4):
    arr5[i]=arr5[i]*matrix[3][2]

for i in range (4):
    matrix[3][i]=matrix[3][i]-arr5[i]
print(matrix)
























































































































































































































































































