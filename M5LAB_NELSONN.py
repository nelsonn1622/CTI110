#cti-110
#NelsonN
#M5LAB
#10/27/17





#to use the turtle

import turtle

def main():
    
    wn = turtle.Screen()      
    t = turtle.Turtle()
    t.speed(8)
    #t.color("purple")
    t.pensize(8)

    colors = ["purple","blue","yellow","pink"]

    for i in range(4):
        t.color(colors[i])
        t.left(85)
        t.forward(45)
        for i in range(8):
            t.forward(100)
            t.right(55)
            t.forward(4)
            t.right(170)
            t.forward(200)
            t.forward (50)
'''
turtle.penup()
turtle.left(180)
turtle.pendown()
''' 

            

main()


