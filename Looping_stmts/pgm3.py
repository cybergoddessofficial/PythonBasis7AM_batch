# a=0
# while(a<10):
#     a+=2
#     print(a)

# lower=1
# upper=10
lower=int(input("enter first limit:"))#2
upper=int(input("enter second limit:"))#10
if(lower>upper):
    print("lower limit should be smaller...")
else:
    while(lower<=upper):#2<=10 3<=10
        if(lower%2==0): #2%2==0
            print(lower) #2
        lower+=1 #3

# i=1
# while(i<=10):
#     if(i%2==0):
#         print(i)
#     i+=1
