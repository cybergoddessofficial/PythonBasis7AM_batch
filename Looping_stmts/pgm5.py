#123->321 reverse of number
num=int(input("enter a number:"))#123
result=0
while(num!=0):
        #123!=0
        #12!=0
        #1!=0
        #0!=0
    reminder=num%10
        #123%10=3=reminder
        #12%10=2=reminder
        #1%10=1=reminder
    result=(result*10)+reminder
        #result=(0*10)+3=0+3=3
        #result=(3*10)+2=32
        #result=(32*10)+1=321
    num=num//10
        #num=123//10=12
        #num=12//10=1
        #num=1//10=0
print(result) #321