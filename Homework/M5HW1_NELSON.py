#CTI 110
#NajahNelson
#Mr. Norris
#Distance Traveled
#10\16

#program that asks speed and num of hrs traveled

#distance = speed * time

def main ():
    print("What is your speed in MPH?")
    speed = int(input())
    print("How many hours have you traveled?")
    hours = int(input())
    for hour in range (1,hours +1):
        distance = speed * hour
        print("hour", hour , "distance", distance)
        #print('distance', distance) 










#START
main()
