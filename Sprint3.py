#Program to wtite
#Cool Stuff with Strings and Dates
#Date written : OCT 26 2023
#Author : SIREESHA KUPPAMPATI
import datetime
import random
print()
print()

Emp_Title = input("Enter the Employee title(Mr/Mrs/Ms): ").title()
Emp_Firstname = input("Enter the Employee first name :    ").title()
Emp_Lastname = input("Enter the Employee last name :    ").title()
Ph_Num = input("Enter the Employee phone Number(###-###-####) : ")
Ph_Num = "(" + Ph_Num[0:3] + ") " + Ph_Num[3:6] + "-" + Ph_Num[6:]

FullEmpName = Emp_Title + ". " + Emp_Firstname + " " + Emp_Lastname
print(f"Employee full name:      {FullEmpName:<25s}")
  
CustCtr = random.randint(1000, 9999)
 
EmpID = Emp_Firstname[0:2] + str(CustCtr) + "-" + Ph_Num[1:5] + "-" + Emp_Lastname[0:2]
EmpID = EmpID.upper()

 
UAlpha = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LAlpha = ("abcdefghijklmnopqrstuvwxyz")
Numbs = ("0123456789")
 
 
while True:
    UserName = input("Enter the User name (10characters only): ")

 
    if UserName == "":
        print("User name cannot be blank - please re-enter.")
    elif len(UserName) != 10:
        print("User name must be 12 digits - please re-enter.")
    elif set(UserName[0]).issubset(UAlpha) == False:
        print("first letter of Usernme must be capital - please reneter.")
    else:
        break
 
NumUpper = 0
NumLower = 0
NumDig = 0
NumSpec = 0
 
while True:
    Password = input("Enter a password: ")
    for i in range(0, len(Password)):
        if set(Password[i]).issubset(UAlpha) == True:
            NumUpper += 1  
        elif set(Password[i]).issubset(LAlpha) == True:
            NumLower += 1
        elif set(Password[i]).issubset(Numbs) == True:
            NumDig += 1
        else:
            NumSpec += 1

    print(NumUpper, NumLower, NumDig, NumSpec)
    
    if Password == "":
        print("Password cannot be Empty please re-enter: ")
    elif len(Password) < 7:
        print("Password should be 6 characters only. ")
    elif NumUpper == 0:
        print("Must contain an upper case letter.")
    elif NumLower == 0:
        print("Must contain a lower case character.")
    elif NumDig == 0:
        print("Must contain a number.")
    elif NumSpec == 0:
        print("Must contain a special character.")
    else:
        break

Emp_Start_Date = datetime.date(2016, 8, 24)
Emp_Birth_Date = datetime.date(2023, 11, 28)
Retirement_Date = datetime.date(2040, 11, 28)
Tday = datetime.date.today()

CurDate = datetime.datetime.now()
CurYear = CurDate.year
CurMonth = CurDate.month
CurDay = CurDate.day    

Till_Bday = Emp_Birth_Date -Tday

Emp_Work_Years = Tday - Emp_Start_Date

Till_Retirement = Retirement_Date - Emp_Start_Date

print("Employee full name:                            ", FullEmpName)
print("Employee Phone number:                         ", Ph_Num)
print("  EmpID:                                       ", EmpID)
print("Employee Username:                             ", UserName)
print("Employee Password:                             ", Password)
print("Employee start date:                           ", Emp_Start_Date)
print("Employee Birth date:                           ", Emp_Birth_Date)
print("Employee Retirement date:                      ", Retirement_Date)
print("How long Employee working with us:             ", Emp_Work_Years)
print("How many days left for Employee birthday :     ", Till_Bday)
print("How many days left for Employee Retirement :   ", Till_Retirement)

