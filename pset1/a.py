annual_salary= 120000
portion_saved= 0.1
total_cost = 1000000
portion_down_payment = 0.25
monthly_salary = annual_salary/12

current_savings = 0

r = 0.04

i=0
while current_savings<(total_cost*portion_down_payment):
    current_savings = current_savings + (current_savings*r/12) + (monthly_salary*portion_saved)
    i=i+1

print(i)