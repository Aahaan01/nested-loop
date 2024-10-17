num=int(input("Please enter a number "))
numlength=0
temp=num
while temp>0:
    numlength=numlength+1
    temp=temp//10
if numlength>=4:
    numlength=numlength//2
    check=0
    while num>0:
        rem=num%10
        if check==numlength:
            midnumber=rem
        elif check==(numlength-1):
            mid2=rem
        num=num//10
        check=check+1
    print("Mid Product", midnumber*mid2)
else:
    print("please enter a number not less than 4 digits")