import turtle

turtle.Screen().bgcolor("purple")

sc=turtle.Screen()
sc.setup(500,500)

turtle.title("Welcome to Turtle class")

board=turtle.Turtle()
board.fillcolor("green")
board.begin_fill()
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.end_fill()



turtle.done()