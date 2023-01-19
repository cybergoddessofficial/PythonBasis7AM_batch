age=int(input("enter your age")) #-369
if((age>18) & (age<60)): #FALSE
    print("you're major")
elif((age<18) & (age>0)): #369<18 TRUE
    print("you're minor")
elif(age>60): #369>60 TRUE
    print("you're retired") #
elif(age<=0):
    print("age must be a positive number")
else:
    print("invalid")