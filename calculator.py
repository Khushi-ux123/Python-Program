def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "cannot divide by zero"
    return x/y
print("SIMPLE CALCULATOR")
print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int (input("Enter choice(1/2/3/4):"))
if choice not in (1,2,3,4):
    print("Wrong Input,Try Again")
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if choice==1:
    print("RESULT:",add(num1,num2))
elif choice==2:
    print("RESULT:",subtract(num1,num2))
elif choice==3:
    print("RESULT:",multiply(num1,num2))
elif choice==4:
    print("RESULT:",divide(num1,num2))
else:
    print("Something Went Wrong,Try Again.")

    
  
    
