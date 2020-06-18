# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:02:14 2020

@author: User
"""


#fixed input
semi_annual_raise = 0.07
return_on_investment = 0.04 / 12
cost_of_house = 1000000
down_payment = 0.25 * cost_of_house 
base_annual_salary = float(input("Enter your starting annual salary: "))
months = 36

current_savings = 0

 
epsilon = 100
#input that changes
initial_high = 1000
high = initial_high
low = 0 
steps = 0
portion_saved = (high + low) // 2



#finding the portion saved using a while loop
while (down_payment - current_savings) != epsilon and (current_savings - down_payment) != epsilon:
    current_savings = 0
    steps += 1
    annual_salary = base_annual_salary
    for month  in range(1, months + 1):
        monthly_rate_of_return = 0.04 / 12

        monthly_deposit = (portion_saved / 1000) * (annual_salary / 12)   
    
        current_savings *= 1 + monthly_rate_of_return
        current_savings += monthly_deposit
        
        if month % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            
            
    prev_portion_saved = portion_saved
    if current_savings > down_payment:
        high = portion_saved
        
    else:
        low = portion_saved
        
    portion_saved = int(round((high + low) / 2))
    
    if prev_portion_saved == portion_saved:
        break
    
if prev_portion_saved == portion_saved and portion_saved == initial_high:
    print('It is not possible to pay the down payment in three years.')

print ("Best savings rate:", portion_saved/1000)  
print ("Steps in bisection search: ", steps)
