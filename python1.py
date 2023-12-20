# Group 19; Artem Babiienko and Sireesha Kuppampati; Nov 1, 2023.

# - - - Task:

# 1. Employee number (must be entered and be 5 characters)
# 2. Employee first name (must be entered – adjust to title case)
# 3. Last name (must be entered – adjust to title case)
# 4. Location of the trip, start date (Must be entered and valid)
# 5. End date (Must be entered and after the start date by no more than 7 days)
# 6. A value to indicate if they used their own car, or if a car was rented (Must be entered and must be the letters O or R only)
# 7. The total kilometers traveled (Must be entered and cannot exceed 2000) - only enter the kilometers if the employee used their own car
# 8. The claim type as standard or executive (S/E) (Must be S or E – adjust to uppercase). Only two validations are required.

# Calculate the number of days based on the start and end dates. Calculate the per diem amount by
# - multiplying the total days by a daily rate of 85.00 per day. The mileage amount is calculated using a
# -- rate of .17 per kilometer if the salesperson used their car, or a rate of $65.00 per day is the salesperson rented a car. 

# The bonus is calculated based on the following:
# -If the number of days is more than 3 add $100.00 to the bonus. If the kilometers are over
# -- 1000 and the salesperson used their own car, add an extra 4 cents per kilometer to the
# --- bonus. If the claim type is Executive add an extra $45.00 per day to the bonus. Finally, if
# ---- the start date is between Dec 15 and Dec 22 add an extra $50.00 per day to the bonus.

# The Claim Amount is calculated as the per diem amount, the mileage amount, and the bonus. The
# - HST is calculated on the Claim Amount using a rate of 15%. The Claim Total is the Claim Amount plus the HST.

# The program will display all input and calculated values to the screen as results. Only display the
# - mileage amount if it is calculated. Just do a basic printout with headings and formatted values.

# Repeat the program until the user enters a termination value either on the first input, or a prompt at
# - the end of the claim output.

import datetime

def calculate_claim_amount(start_date, end_date, used_car, kilometers, claim_type):
    
    # Calculate the number of days based on the start and end dates
    num_days = (end_date - start_date).days + 1
    # Calculate the per diem amount
    daily_rate = 85.00
    per_diem = num_days * daily_rate

    # Calculate the mileage amount
    if used_car:
        mileage_rate = 0.17
        mileage_amount = min(kilometers, 2000) * mileage_rate
    else:
        mileage_amount = 65.00

    # Calculate the bonus amount
    bonus = 0
    if num_days > 3:
        bonus += 100.00
    if used_car and kilometers > 1000:
        bonus += 0.04 * (kilometers - 1000)
    if claim_type == 'E':
        bonus += 45.00
    if start_date.month == 12 and 15 <= start_date.day <= 22:
        bonus += 50.00

    # Calculate the Claim Amount
    claim_amount = per_diem + mileage_amount + bonus

    return per_diem, mileage_amount, bonus, claim_amount


while True:
    employee_number = input("Enter employee number (5 characters): ")
    if employee_number == 'exit':
        break
    employee_first_name = input("Enter employee first name: ").title()
    employee_last_name = input("Enter employee last name: ").title()
    location = input("Enter location of the trip: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    use_own_car = input("Did employee use their own car (O) or rent a car (R)? ").upper()
    if use_own_car == 'O':
        kilometers = int(input("Enter total kilometers traveled: "))
    else:
        kilometers = 0 
    claim_type = input("Enter claim type (S for Standard, E for Executive): ").upper()

    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    per_diem, mileage_amount, bonus, claim_amount = calculate_claim_amount(
        start_date, end_date, use_own_car == 'O', kilometers, claim_type)

    hst_rate = 0.15
    hst_amount = claim_amount * hst_rate
    claim_total = claim_amount + hst_amount


    print("\n- - - Travel Claim Information: - - -")
    print("Employee Number:", employee_number)
    print("Employee First Name:", employee_first_name)
    print("Employee Last Name:", employee_last_name)
    print("Location of the Trip:", location)
    print("Start Date:", start_date.strftime("%Y-%m-%d"))
    print("End Date:", end_date.strftime("%Y-%m-%d"))
    print("Used Own Car (O) or Rented Car (R):", use_own_car)
    if use_own_car == 'O':
        print("Total Kilometers Traveled:", kilometers)
    print("Claim Type (S for Standard, E for Executive):", claim_type)
    print("\n- - - Claim Details: - - -")
    print("Number of Days:", (end_date - start_date).days + 1)
    print("Per Diem Amount: ${:.2f}".format(per_diem))
    if use_own_car == 'O':
        print("Mileage Amount: ${:.2f}".format(mileage_amount))
    print("Bonus Amount: ${:.2f}".format(bonus))
    print("Claim Amount: ${:.2f}".format(claim_amount))
    print("HST Amount (15%): ${:.2f}".format(hst_amount))
    print("Claim Total: ${:.2f}".format(claim_total))
    print("- - -")
    print("\n")

print("Bye!")
