name=input("Please enter your name ")
char=input("Please enter a character ")

i=0
count=0
while i<len(name):
    if name[i]==char:
        count=count+1
    i=i+1

print("The total number of times a", char, "has occured", count)