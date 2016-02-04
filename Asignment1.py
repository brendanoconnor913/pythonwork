

# Notes on possible improvements from the keys
# Declare all of the variables you will need at the top of the program
# Align all of the variables so the = align in a column for each variable
# Make notes not only between lines and in clearly defined chunks but at the end of complicated lines







########################################################################
##
## CS 101
## Program 1
## Brendan  
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com 
## Created 8/28/2015
## Due 9/6/2015
##
## PROBLEM : The problem is Mark is stuck on Mars and needs to determine how
## he will be able to make it with the food rations and potatoe plants he has.
##
## ALGORITHM : 
##      1. We will gather input from Mark (# of rations, # of cals per day,
##          and how much farmland he has to work with)
##      2. Next we will use the assumed values for calculations on his time 
##          and what he needs.
##      3. Finally we will output the number from our calculations to let Mark
##          know how much time he has left,
## 
## ERROR HANDLING:
##      None for this program
##
## OTHER COMMENTS:
##      
##
########################################################################

# Make sure assignment is in accordance with the grading rubric


# We will start by collecting basic info from Mark for the calculations
rations = float(input("How many food ration packs do you have: "))
cals = float(input("Estimate how many calories you plan on burning per day: "))
frmland = float(input("Estimate in square meters how much farmland you have \
    to devote to growing potatoes: "))

# We will assume the following for the calculations:
# Mark will use all of his farmland available
# He has all of the resources needed to grow the potatoes
# He will burn the exact same ammount of calories inputted each day
#
# 1 ration = 2,000 calories
# 1 m^2 of land needs 1/10 m of soil to grow potatoes
# 1 m^3 of land needs 40 L of water to grow potatoes
# potatoes will grow at a rate of .006 Kg/ 1 (m^2 * day) - not m^3
# 1 Kg of potatoes = 700 cals

ration_cals = rations * 2000
days_of_farming = ration_cals / cals
cubic_land_needed = frmland / 10
water_needed = cubic_land_needed * 40

# Calculating the potatoes he will have when he runs out of rations
potatoes_kg = .006 * frmland * days_of_farming
cals_of_potatoes = 700 * potatoes_kg
days_of_potatoes = cals_of_potatoes / cals
total_days_left = days_of_potatoes + days_of_farming

# Now we output all of the relevant information to Mark
print("You will survive ", days_of_farming, " days on rations \n") 
print("You will need ", cubic_land_needed, " meters of soil")
print("This will require", water_needed, " L of water")
print("You can grow ", potatoes_kg, " kg of potatoes \n") 
print("The potatoes will give you ", days_of_potatoes, " days of calories") 
print("This will give you a total of ", total_days_left, "days")
