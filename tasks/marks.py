def student(marks):
    if n<25:
        print("You Failed")
    elif n>=25 and n<45:
        print("You got D grade")
    elif n>=45 and n<60:
        print("You got C grade")
    elif n>=60 and n<70:
        print("You got B grade")
    elif n>=70 and n<80:
        print("You got A grade")
    elif n>=80 and n==100:
        print("You got O grade")
    else:
        print("Invalid")

n=int(input("enter the marks :"))
student(n)
