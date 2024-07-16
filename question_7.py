print("Matrix 1 : ")
row=int(input("Enter rows : "))
column=int(input("Enter column : "))
y=[]
for i in range(row):
    x=[]
    for j in range(column):
        z=int(input("Enter number : "))
        x.append(z)
    y.append(x)
    del x
    print("\n")
print("Matrix 1 : ")
print(y)

print("Matrix 2 : ")
row2=int(input("Enter rows : "))
column2=int(input("Enter column : "))
m=[]
for i in range(row):
    n=[]
    for j in range(column):
        z=int(input("Enter number : "))
        n.append(z)
    m.append(n)
    del n
    print("\n")
print("Matrix 2 :\n ")
print(m)

add=[]  
for i in range(row):
    temp=[]
    for j in range(column):
        temp.append(y[i][j]+m[i][j])
    add.append(temp)
    del temp
print("Matrix Addition :\n ")
print(add)

sub=[]  
for i in range(row):
    temp2=[]
    for j in range(column):
        temp2.append(y[i][j]-m[i][j])
    sub.append(temp2)
    del temp2
print("Matrix subtraction:\n ")
print(sub)
    
