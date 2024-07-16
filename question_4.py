x=int(input("Enter Number : "))
temp=x
result=0
while x>0:
    rem=int(x%10)
    x=x//10
    result=result*10+rem
if(temp==result):
    print("Palindrome Number")
else:
    print("Not Palindrome")
