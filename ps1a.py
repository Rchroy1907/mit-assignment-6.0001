# Happy Coding!
"""
Objective:
Part A:
House Hunting:
story:
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part A, we are going to determine how long it will take you to save enough
money to make the down payment.
 Name- Sumanta Mandal 
 Branch:Computer Science Engineering 
 Roll No:18/CSE/041
 
"""

# Part A: House Hunting


annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
monthly_savings = (annual_salary / 12) * portion_saved

total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25 #25%
down_payment = total_cost * portion_down_payment

annual_return = 0.04
current_savings = 0.0

number_of_months = 0

while current_savings < down_payment:
    current_savings += monthly_savings + ((current_savings * annual_return) / 12)
    number_of_months += 1

print('Number of months: {}'.format(number_of_months))
