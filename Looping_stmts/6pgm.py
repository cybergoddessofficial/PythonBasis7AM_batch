#123->321 reverse of number
num=int(input("enter a number:"))#123
result=0
while(num!=0):
    reminder=num%10
    result = (result * 10) + reminder
    num = num // 10
print(result)
#TasK:sum of cube 123=(1*1*1)+(2*2*2)+(3*3*3)
#result=(reminder**3)+result