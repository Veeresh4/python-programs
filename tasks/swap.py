def swap(x,y):
    print("before swap :", x,y)
    x=x+y
    y=x-y
    x=x-y
    return x,y
x=int(input("enter the number :"))
y=int(input("enter the number :"))
result=swap(x,y)
print("after swap :",result)    
