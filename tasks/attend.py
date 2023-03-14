def student(held,attended):
    percentage=(y/float(x))*100
    print(percentage)
    if percentage >75:
        print("You are eligible to take exam")
    else:
        print("You are not eligible to take exam")


x=int(input("number of classes held :"))
y=int(input("Number of classes attended :"))
student(x,y)