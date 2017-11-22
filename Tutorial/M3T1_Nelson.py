#CTI-110
#M3T1- Area of Retangles
#Najah Nelson
#Mr. Norris
#Sept 13, 2017

#Calculate area of two rectangles

firstWidth = int(input("width of first?"))
firstLength = int(input("length of first?"))


secondWidth = int(input("width of second?"))
secondLength = int(input("length of second?"))

firstArea = firstWidth * firstLength
secondArea = secondWidth * secondLength

if firstArea > secondArea:
    print ('first is bigger')

else:
    if firstArea < secondArea:
        print('second is bigger')
    else:
        print('they are equal size')
print('done')
