" turtle demo "

import turtle

#pylint: disable=C0103

def fun():
    " run forward "
    if running:
        print("Hello")
        henry.forward(50)
        henry.left(60)
        turtle.Screen().ontimer(fun,10)


running = True
window = turtle.Screen()
henry = turtle.Turtle()

fun()
#running = False

window.mainloop()
