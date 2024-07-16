#type 1
x=int(input("Enter Number of rows for right pyramid printing : "))
for i in range(1,x+2):
    for j in range(1,i):
        print("*",end="")
    print("\n")
#type 2  
x=int(input("Enter Number of rows for right pyramid printing : "))
for i in range(x+1,1,-1):
    for j in range(1,i):
        print("*",end="")
    print("\n")   
#type 3  
y=int(input("Enter Number of rows for pyramid printing : "))
m=y
for x in range(1,y+1):
    for n in range(m,1,-1):
        print(" ",end="")
    for j in range(1,x+1): 
        print("*",end=" ")
    m=m-1
    print("\n")
    
            
            

    

        
