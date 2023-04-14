"""
Tip calculator project from the 100 days python course
"""

#Get the amount of the bill
bill_value = float(input("How much is the bill? $"))
#Show the tip options and get the selected one
selected_tip_option = int(input('''
How much tip you'd like to give?
  1. 10%
  2. 12%
  3. 15%

Select and option (1-3): '''))
#Ask for the number of the people
number_of_people = int(input("How many people to split the bill? "))
#Tips values
tips_value = [10, 12, 15]
#The calculated tip value
tip_value = (tips_value[selected_tip_option - 1] / 100) + 1
#How much needs to be paid per person
pay_per_person = (bill_value / number_of_people) * tip_value
#Showing the result
print(f"--------------------------\nYou need to pay: ${pay_per_person:.2f}")