x=int(input("Enter Number for finding factorial : "))
if x==0:
    print("Factorial of 0 is 1 ")
    exit()
def fact(n):
    i=n-1
    while i>1:
        n=n*i
        i=i-1
    return n 
result=fact(x)
print(f"factorial of {x} is {result}")