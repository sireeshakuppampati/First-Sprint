#Program to Maintanace schedule
#for XYZ Company
#Date written : OCT 27 2023
#Author : SIREESHA KUPPAMPATI
import datetime
import random
print()
print()

#Declaring th eConstants
SAL_VALUE = 0.1
print()

#user inputs
UserName = input("Enter the user name: ")
cost_Item = float(input("Enter the  purchase cost of the item: "))
Purchase_Date = input("Enter the purchase date of the item(YYYY-MM-DD): ")
Purchase_DateDSP = datetime.datetime.strptime(Purchase_Date, "%Y-%m-%d")

Basic_Cln = Purchase_DateDSP + datetime.timedelta(days = 10)
print(Basic_Cln)

Tube_Fluid_Cln = Purchase_DateDSP + datetime.timedelta(days = 21)
print(Tube_Fluid_Cln)

CurYear = Purchase_DateDSP.year
CurMonth = Purchase_DateDSP.month
CurDay = Purchase_DateDSP.day
print()

if CurMonth == 1:
    Major_Insp = datetime.date(CurYear , CurMonth + 6, CurDay +1)
    print(Major_Insp)
elif CurMonth == 2:
    Major_Insp = datetime.date(CurYear , CurMonth + 6, CurDay -1)
    print(Major_Insp)
elif CurMonth == 3:
    Major_Insp = datetime.date(CurYear , CurMonth + 6, CurDay +1)
    print(Major_Insp)
elif CurMonth == 4:
    Major_Insp = datetime.date(CurYear , CurMonth + 6, CurDay )
    print(Major_Insp)
elif CurMonth == 5:
    Major_Insp = datetime.date(CurYear , CurMonth + 6, CurDay +1)
    print(Major_Insp)
elif CurMonth == 6:
    Major_Insp = datetime.date(CurYear , CurMonth + 6, CurDay)
    print(Major_Insp)
elif CurMonth == 7:
    Major_Insp = datetime.date(CurYear + 1 , CurMonth - 6, CurDay +1)
    print(Major_Insp)
elif CurMonth == 8:
    Major_Insp = datetime.date(CurYear + 1, CurMonth - 6, CurDay +1)
    print(Major_Insp)
elif CurMonth == 9:
    Major_Insp = datetime.date(CurYear + 1, CurMonth - 6, CurDay)
    print(Major_Insp)
elif CurMonth == 10:
    Major_Insp = datetime.date(CurYear + 1, CurMonth - 6, CurDay +1)
    print(Major_Insp)
elif CurMonth == 11:
    Major_Insp = datetime.date(CurYear + 1, CurMonth -6, CurDay)
    print(Major_Insp)
elif CurMonth == 12:
    Major_Insp = datetime.date(CurYear + 1, CurMonth -6, CurDay +1)
    print(Major_Insp)
else:
    print("Enter the proper date")
print()
print()
Salvage = cost_Item * SAL_VALUE
Amortization = (cost_Item - Salvage) / 150

print("     Maintanace Schedule Of XYZ Company          ")
print()
print("     UserName:                                         " ,UserName)
print("     cost Item:                                        ", cost_Item)
print("     Basic cleaning date after 10 days is:             ", Basic_Cln)
print("     Tube and Fliud cleaning date after 21 days:       ", Tube_Fluid_Cln)
print("     Major Inspection date after 6 months:             ",Major_Insp)
print("     Salvage cost :                                    ", Salvage)
print()
print("     Monthly Amortization for 15 years life:           ", Amortization)
print()
