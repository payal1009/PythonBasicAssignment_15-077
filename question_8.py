str=(input("Enter String for finding maximum character : "))
count=0
max=0
for i in range(len(str)):
    temp=str[i]
    for j in range(len(str)):
        if(temp==str[j]):
            count=count+1
    if(max<count):
        max=count
        char=str[i]
    count=0
print(f" Maximun frequency of character {char} in string {str}")