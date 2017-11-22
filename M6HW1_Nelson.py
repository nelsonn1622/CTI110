#CTI-110
#Najah Nelson
#M6HW1
#11/6/17




def main():
    calc_average()
    
    


def calc_average():
    Grade1 = int(input('What is your score for Grade1?'))
    print (determine_grade(Grade1))
    Grade2 = int(input('What is your score for Grade2?'))
    print (determine_grade(Grade2))
    Grade3 = int(input('What is your score for Grade3?'))
    print (determine_grade(Grade3))
    Grade4 = int(input('What is your score for Grade4?'))
    print (determine_grade(Grade4))
    Grade5 = int(input('What is your score for Grade5?'))
    print (determine_grade(Grade5))
    avg= (Grade1 + Grade2 + Grade3 + Grade4 + Grade5)
    avg = avg /5
    print('average is:',avg)
    
def determine_grade(grade):
    if grade >= 90:
        answer = "A"
    elif grade >= 80 and grade < 90:
        answer = "B"
    elif grade  >= 70 and grade < 80:
        answer = "C"
    elif grade >= 60 and grade <70:
        answer = "D"
    elif grade < 60:
        answer = "F"
    return answer
    



main()
    
                 


