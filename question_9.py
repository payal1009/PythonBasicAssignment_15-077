myDict = {'Ashwin': 100, 'rakesh': 9,
 'Ravindra': 25, 'yash': 200, 'sai': 32}

m=list((myDict.items())) # convert to list 
m.sort() # sort list
myDict=dict((m)) #aain convert to dictionary
print(myDict)