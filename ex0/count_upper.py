#Arun Woosaree

string = input() #get input
counter=0

for char in string: #count uppercase letters
    if char.isupper():
        counter +=1

print(counter) #display output
