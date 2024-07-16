
x=int(input("enter start value : "))
y=int(input("enter last number : "))
l=[]
if x<=1 or y<x:
    print("Invalid Input")
    exit()
for i in range(x,y):
    for j in range(2,x):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)


