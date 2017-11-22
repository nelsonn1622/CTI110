#CTI-110
#Najah Nelson
#Mr. Norris
#M2HW2:Tip, Tax and Total

foodCost = float(input('Please enter the foodCost: '))
tipAmount = 0.18 * foodCost
salesTax = 0.07 * foodCost
totalCost = foodCost + tipAmount + salesTax
print('The tipAmount: $' + format(tipAmount, '0.2f'))
print('the salesTax is: $' + format(salesTax, '0.2f'))
print('totalCost is: $' + format(foodCost + tipAmount + salesTax, '0.2f'))
