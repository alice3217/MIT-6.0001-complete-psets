# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:19:50 2020

@author: User
"""


#user unput
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#fixed input
portion_down_payment = 0.25 * total_cost 
current_savings = 0
monthly_rate_of_return = 0.04 / 12
monthly_deposit = portion_saved * (annual_salary / 12)

months = 0

#increment the current savings and count months
while current_savings < portion_down_payment:
    months += 1
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_deposit
    
print ("Number of months:", months)