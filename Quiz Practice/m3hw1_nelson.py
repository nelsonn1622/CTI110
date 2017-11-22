#CTI-110
#
#NajahN
#9/20
#ask the user the temperature outsdide


def main():
    hot=80
    cold=60

    if temp > hot:
        answer = "A/C"
    elif temp <= cold:
        answer = "Heat"
    elif temp >= cold and temp <=hot:
        answer = "Fan"
    else:
        answer = "ERROR"

    #print the answer
    print ("at that temperature, you should use the ", answer)

#ask the temperature outside
temp= int(input("what's the temperature today? (in F) "))

#calculate the answer
#it's either hot, temerate, or cold

hot=80
cold=60

if temp > hot:
    answer = "A/C"
elif temp <= cold:
    answer = "Heat"
elif temp >= cold and temp <=hot:
    answer = "Fan"
else:
    answer = "ERROR"

#print the answer
print ("at that temperature, you should use the ", answer)

#start the program
main()
