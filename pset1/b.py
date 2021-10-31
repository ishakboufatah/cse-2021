"""
Created on Wed  7 11:37:28 2021

@author: ishak
"""
print('Hi :)')
annual_salary= int(input('Enter your annual salary:'))
portion_saved= float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost= int(input("Enter the cost of your dream home:"))
semi_annual_raise= float(input("Enter the semiannual raise, as a decimal:"))


portion_down_payment=0.25
current_savings=0
r = 0.04 
Number_of_months=1
while current_savings<total_cost*(portion_down_payment):
    monthly_salary=annual_salary/12
    Number_of_months=Number_of_months+1
    current_savings=current_savings+monthly_salary*portion_saved
    current_savings=current_savings*r/12+current_savings
    if Number_of_months%6 == 0:
        annual_salary=annual_salary+annual_salary*semi_annual_raise

print('Number of months:',Number_of_months)


