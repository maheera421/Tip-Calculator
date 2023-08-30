
print("""
 _____ _         _____       _            _       _             
|_   _(_)       /  __ \     | |          | |     | |            
  | |  _ _ __   | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  | | | | '_ \  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | | | | |_) | | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
  \_/ |_| .__/   \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
        | |                                                     
        |_|                                                     
""")
print("WELCOME TO TIP CALCULATOR!!!\n")

#input from user
bill= input("What is the total bill? $")
tip= input("What percentage tip would you like to give? 10%, 12% or 15%? ")
ppl= input("How many people to split the bill between? ")

#changing datatypes
Bill= float(bill)
Tip= int(tip)
Ppl= int(ppl)

#solving mathematically
tip_of_bill= (Tip / 100) * Bill
new_bill= Bill + tip_of_bill
split_bill= new_bill / Ppl

#rounding to 2 decimal places
Split_bill= round(split_bill, 2)
Split_bill= "{:.2f}".format(split_bill)

#displaying output
print("\n-----------------------")
print(f"Each person should pay: ${Split_bill}")
