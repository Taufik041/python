import random

n=random.randrange(1000,9999)
gentd=list(int(d) for d in str(n))
print(n)

for i in range(10):
    guess=[]
    print("Enter your 4 digit code:")
    num=int(input())
    guess=list(int(j) for j in str(num))
    j=0
    str=""

    for j in range(4):
        if guess[j]==gentd[j]:
            str=str+"R"
        elif guess[j] in gentd:
            str=str+"A" 
        else:
            str=str+"W"
        j=j+1

    print(str)
    if str=="RRRR":
        print("Your code is correct !!")
        break


if (str!="RRRR"):
    print("Your code is not correct !!")