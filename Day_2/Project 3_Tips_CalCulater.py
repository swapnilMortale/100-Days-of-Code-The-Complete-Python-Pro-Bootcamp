print("Welcome to The tip Calculator...!\n")
bill=float(input("What Was The Total Bill $ ?  "))
tip=float(input("What perscentage tip would you like to give 10 12 15 18 "))
pepole = int(input("How many pepole to split this Bill ?"))
tip_as_perscentage= tip / 100
total_tip_amount= bill * tip_as_perscentage
total_bill = bill +total_tip_amount
bill_per_person =total_bill /pepole
final_amount= round(bill_per_person,2)
print(f"Each Person should pay : ${final_amount}")
