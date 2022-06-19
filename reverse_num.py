#Read a number from keyboard and print it in reverse.

num=int(input("enter a number:"))
rn=0
while num !=0:
    temp=num %10
    rn=rn*10+temp
    num=num//10
print("reverse number of:",n," is:")
print(rn)