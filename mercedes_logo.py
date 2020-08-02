
import turtle

myPen = turtle.Turtle()
myPen.shape("turtle")
#myPen.speed(200)

myPen.color("#2F4F4F")
myPen.pensize(4)


def clearScreen():
  myPen.penup()
  myPen.goto(0,0)
  myPen.setheading(0)
  myPen.clear()
  myPen.pendown()
  
def drawMercedesLogo():
  clearScreen()
  myPen.circle(150)
  myPen.left(90)
  myPen.penup()
  myPen.forward(150)
  myPen.pendown()
  myPen.forward(150)
  myPen.penup()
  myPen.forward(-150)
  myPen.left(120)
  myPen.pendown()
  myPen.forward(150)
  myPen.penup()
  myPen.forward(-150)
  myPen.left(120)
  myPen.pendown()
  myPen.forward(150)
  myPen.penup()
  myPen.forward(-150)
  myPen.left(120)
