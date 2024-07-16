n=int(input("Enter size of array : "))
l=[]
for i in range(n):
    l.append(int(input("Enter element : ")))
print("Unsorted array : ")
print(l)
for i in range(len(l)):
    
    for j in range(0,i+1):
        if(l[i]<l[j]):
           c=l[i]
           l[i]=l[j]
           l[j]=c
print("Insertion Sort output : ") 
print(l,"\n")