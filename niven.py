num=int(input("Enter the number and check whether it is a niven number or not:"))
sum=0
temp=num
while(temp!=0):
    d=temp%10
    sum=sum+d
    temp=temp//10
if(num%sum==0):
    print("It is a niven number")
else:
    print("It is not a niven number")        
