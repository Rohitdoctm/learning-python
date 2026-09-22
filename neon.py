num=int(input("Enter the num and check whether it is a Neon numbrer:"))
sqrt=num*num
sum=0
while(sqrt!=0):
    d=sqrt%10
    sum=sum+d
    sqrt=sqrt//10
if(sum==num):
    print("It is a neon number")
else:
    print("It is not a neon number")        
