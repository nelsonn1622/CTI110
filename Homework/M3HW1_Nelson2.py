#CTI-110
#NajahN
#9/20
#M3HW1: Age Classifier



    
  
#ask the user thier age
age = int(input("what's your age? "))

#define age
if age <= 1:
    answer = "An infant"
elif age >= 1 and age <= 13:
    answer = "A child"
elif age  >= 13 and age < 20:
    answer = "A teenager"
elif age  >= 20:
    answer = "An adult"

#get answer
print (" you are, " , answer )











  
  






