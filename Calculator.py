print("Calculator")
a=int(input("enter your number1="))
b=int(input("enter your number2="))
c=input("enter operation=")
if(c=="+"):
    print("the sum of a and b is",a+b)
elif(c=="-"):
    print("the diff of a and b is",a-b)
elif(c=="*"):
    print("the product of a and b is",a*b)
elif(c=="/"):
    print("the divide of a and b is",a/b)
else:
    print("invalid operation")
    