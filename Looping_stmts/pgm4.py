#find sum of n numbers b/w 2 limits
lower=int(input("enter first limit:"))#2
upper=int(input("enter second limit:"))#10
sum=0
if(lower>upper):
    print("lower limit should be smaller...")
else: #2+3+4+5+6=
    while(lower<=upper):#2<20 3<20....6<=6
        sum+=lower #sum=sum+lower 2+3=5=sum
        lower+=1 #4
    print("sum is:",sum)
