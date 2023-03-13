def students(rollnumber):
    while x in rollnumber:
        print("Student is present")
        break
    else:
        print("student is absent")

rollnumber=[10,11,14,16,19,25]
x=int(input("enter the number :"))
students(rollnumber)