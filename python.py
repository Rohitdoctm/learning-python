num=int(input("Enter the number and find the sum of the digit:"))
s=0
while(num>0):
    d=num%10
    s=s+d
    num=num//10
print("The sum of the number is:",s)    
