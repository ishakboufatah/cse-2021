
#python file
"""
Created on Tus JUIL  6 14:18:48 2021

@author: ishak
"""
annual_salary= int(input('Enter your annual salary:'))
portion_saved= float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost= int(input("Enter the cost of your dream home:"))
monthly_salary=annual_salary/12
portion_down_payment=0.25
current_savings=0
r = 0.04
Number_of_months=1
while current_savings<total_cost*(portion_down_payment):
    Number_of_months=Number_of_months+1
    current_savings=current_savings+monthly_salary*portion_saved
    current_savings=current_savings*r/12+current_savings

print('Number of months:',Number_of_months)

