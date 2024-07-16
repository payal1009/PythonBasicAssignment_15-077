l=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Enter number to search : "))
status=0
for y in range(len(l)+1):
    if(y==x):
        status=1
        break        
if status==1:
    print(f"Element {x} found in given list")
else:
    print(f"Element {x} not found in given list")
    