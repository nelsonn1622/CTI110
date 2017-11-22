#CTI-110
#Najah Nelson
#M6LAB
#10/30/17



def main():
    name= input("whats your name?")
    greet(name)
    age= int(input("how old are you?"))

    cat=ageCategory(age)
    print("you are",cat)

def greet(name):
    print("hello", name)
        


def ageCategory(age):
         
    if age <= 1:
        answer = "An infant"
    elif age >= 1 and age <= 13:
        answer = "A child"
    elif age  >= 13 and age < 20:
        answer = "A teenager"
    elif age  >= 20:
        answer = "An adult"
    return answer


        
    











main()
