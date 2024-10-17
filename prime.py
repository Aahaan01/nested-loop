lower=int(input("Please enter a lower range "))
upper=int(input("Please enter a upper range "))

for i in range(lower,upper):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print("break")
                break
        else:
            print(i)