# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:05:36 2020

@author: ishak
"""

annual_salary= float(input('Enter your starting salary:'))
BB=annual_salary
total_cost= 1000000
semi_annual_raise= 0.07


portion_down_payment=0.25
current_savings=0
r = 0.04
Number_of_months=1




epsilon=1
numGuesses=0
low=0
high=10000
portion_saved=(high+low)/2.0
portion_saved1=0000
while abs(portion_saved1-portion_saved)>epsilon:
#while current_savings-100<=total_cost*(portion_down_payment):
    current_savings=0
    #♥print('low = '+str(low)+' high = ' + str(high) +' portion_saved= ' + str(portion_saved))
    numGuesses+=1
    current_savings=0.0
    annual_salary=BB
    for Number_of_months in range(36):
        portion_saved1=portion_saved
        
        Number_of_months+=1
        monthly_salary=annual_salary/12
        current_savings=current_savings+monthly_salary*(portion_saved/10000)
        current_savings=current_savings*r/12+current_savings
        if Number_of_months%6 == 0:
            annual_salary=annual_salary+annual_salary*semi_annual_raise 
    
        
    if current_savings<=total_cost*(portion_down_payment):
        low=portion_saved
    else:
        high=portion_saved
    portion_saved=(high+low)/2.0
  
if total_cost*(portion_down_payment)-current_savings<=10000:
    print("current_savings",current_savings)
    print("Best savings rate:",int(portion_saved)/10000)
    print('Steps in bisection search: '+str(numGuesses))
else:
    print("It is not possible to pay down payment in three years")
