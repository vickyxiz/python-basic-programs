a=int(input("enter a number:"))
if(a<0):
    print("enter a postive number !!!")
else:
    sum_of=0
    
    for i in range(1,a+1):
        sum_of+=i
    print("The total sum is:",sum_of)
