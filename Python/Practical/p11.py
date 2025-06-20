"""
KALYAN JWELLERS : 

M 
>  65
purchase > 2lk - 3lk    20% 
purchase > 3lk - 5lk 	30% 
purchase > 5lk  	35% 


<65
purchase > 2lk - 3lk    10% 
purchase > 3lk - 5lk 	20% 
purchase > 5lk  	25% 



F
>  65
purchase > 2lk - 3lk    25% 
purchase > 3lk - 5lk 	35% 
purchase > 5lk  	40% 


<65
purchase > 2lk - 3lk    15% 
purchase > 3lk - 5lk 	25% 
purchase > 5lk  	30% 


------------------------------------------------------------
Enter your name : 
Enter gender : 
Enter age : 

Enter product : Ring 
Enter product gram : 20  
current gold price (1 grm) : 5752

-------------------------------------
TOTAL GOLD RATE :  XXXXX 


Making charges (1 gram)  : 845
Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

---------------------------------------
TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG



DISCOUNT :   25 (AUTOMATIC) 
DIS- AMOUNT : except (making charges) 
-----------------------------------------
total net amount : 

--------------------------------------------
HINT : variables , input , conditional statements 

"""
name = input("Enter your name: ")
gender = input("Enter gender: ")
age = int(input("Enter your age: "))

product = input("Enter product: ")
product_gram = int(input("Enter product gram: "))
curr_gold_rate = 9607

total_rate = product_gram * curr_gold_rate

making_charges = 845
total_making_charges = product_gram * making_charges

total_amount = total_rate + total_making_charges

if gender == "male" or gender == "m" or gender == "M" or gender == "Male":
    if age >= 65:
        if (total_amount >= 200000 and total_amount < 300000):
            discount = 20
        elif (total_amount >= 300000 and total_amount < 500000):
            discount = 30
        elif (total_amount >= 500000):
            discount = 35
        else:
            discount = 0
    elif age < 65:
        if (total_amount >= 200000 and total_amount < 300000):
            discount = 10
        elif (total_amount >= 300000 and total_amount < 500000):
            discount = 20
        elif (total_amount >= 500000):
            discount = 25
        else:
            discount = 0
    else:
        discount = 0
elif gender == "female" or gender == "f" or gender == "F" or gender == "Female":
    if age >= 65:
        if (total_amount >= 200000 and total_amount < 300000):
            discount = 25
        elif (total_amount >= 300000 and total_amount < 500000):
            discount = 35
        elif (total_amount >= 500000):
            discount = 40
        else:
            discount = 0
    elif age < 65:
        if (total_amount >= 200000 and total_amount < 300000):
            discount = 15
        elif (total_amount >= 300000 and total_amount < 500000):
            discount = 25
        elif (total_amount >= 500000):
            discount = 30
        else:
            discount = 0
    else:
        discount = 0
else:
    print("Invalid input")

print(f"Discount = {discount}%")

discount_amt = (total_amount * discount) / 100
print(f"Discount amount without the making charges = ₹{discount_amt}.")

total_net_amount = total_amount - discount_amt
print(f"Total net amount to be paid with discount = ₹{total_net_amount}.")