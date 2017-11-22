#CTI-110
#NajahN
#Mr. Norris
#M3HW2- Sofware Sales

#define the cost of one package
Onepackage = 99

#define discount values
discount10 = 0.10
discount20 = 0.20
discount30 = 0.30
discount40 = 0.40

Quantity = float(input('please enter the Quantity: '))
total = Quantity * Onepackage

#discount total
discountTotal1 = (total * discount10)
discountTotal2 = (total * discount20)
discountTotal3 = (total * discount30)
discountTotal4 = (total * discount40)

#final total
finalSum1 = (total - discountTotal1)
finalSum2 = (total - discountTotal2)
finalSum3 = (total - discountTotal3)
finalSum4 = (total - discountTotal4)
#creat stipulations
if Quantity < 10:
    print('no discount applied')
    print('the total is', total)
elif Quantity >= 10 and Quantity < 20:
    print('discount of 10% ')
    discountTotal1 = total * discount10
    finalSum1 = total - discountTotal1
    print('your total today is', format(finalSum1,'0.2f'))
elif Quantity >= 20 and Quantity < 50:
    print('discount of 20%')
    discountTotal2 = total * discount20
    finalSum2 = total - discountTotal2
    print('your total today is', format(finalSum2, '0.2f'))
elif Quantity >= 50 and Quantity < 100:
    print('discount of 30%')
    discountTotal3 = total * discount30
    finalSum3 = total - discountTotal3
    print('your total today is', format(finalSum3, '0.2f'))
elif Quantity >= 100:
    print('discount of 40%')
    discountTotal4 = total * discount40
    finalSum4 = total - discountTotal4
    print('your total today is', format(finalSum4, '0.2f'))
    













