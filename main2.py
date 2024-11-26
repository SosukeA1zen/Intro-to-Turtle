import turtle

turtle.Screen().bgcolor("purple")

sc=turtle.Screen()
sc.setup(500,500)

turtle.title("Welcome to Turtle class")

board=turtle.Turtle()
board.fillcolor("black")
board.begin_fill()
board.forward(100)
board.left(120)#
board.forward(100)
board.left(120)#
board.forward(100)
board.end_fill()
board.penup()
board.right(150)
board.forward(50)
board.pendown()
board.begin_fill()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
board.end_fill()
turtle.done()