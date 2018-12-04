import random
import turtle

#보드

n = 10
size = 500

swidth = 600
sheight = 600

def drawGoBoard(cell_num, grid_size, board):

    cell_size = grid_size / cell_num

    turtle.setup(swidth, sheight)
    turtle.tracer(0,0)

    t=turtle.Turtle()
    t.hideturtle()
    t.penup()

    #draw a grid

    t.shape('circle')
    t.pencolor('gray')
    t.shapesize(1)
    for row in range(cell_num+1):
        for col in range(cell_num+1):
            t.setposition(-grid_size/2 + col * cell_size, grid_size/2 - row * cell_size)
            if board[row][col] == 2:
                          t.fillcolor('white')
                          t.stamp()
            if board[row][col] == 1:
                t.fillcolor('black')
                t.stamp()



        turtle.update()
    turtle.done()

def getRandomBoard(cell_num):
    return [[random.randint(0,2) for i in range(cell_num+1)] for j in range(cell_num+1)]





board = getRandomBoard(n)

print(board)

drawGoBoard(n, size, board)


#코드


