# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:54:38 2020

@author: User
"""

#user input
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))


#fixed input
portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0


#increment the current savings and count months
while current_savings < portion_down_payment:
#fixed input
    monthly_rate_of_return = 0.04 / 12

    monthly_deposit = portion_saved * annual_salary / 12
    months += 1
#to check if the months are multiples of 6 so that you can increase annual salary   
    if months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
    
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_deposit
    
print ("Number of months:", months)