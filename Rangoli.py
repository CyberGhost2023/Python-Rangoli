# Using turtle library
import turtle as tu

# setting background color
tu.bgcolor('black')
# setting speed of pen
tu.speed(0)


# Function to draw Swasthik symbol
def drawSwastika():
    x=300
    y=90
    z=180
    tu.pencolor('red')#choose swastika color
    tu.pensize(25) #choose swastika pensize
    # draw right bottom
    tu.forward(x)
    tu.right(y)
    tu.forward(x)
    tu.left(z)
    tu.forward(x)
    tu.left(y)
    # draw left top
    tu.forward(2*x)
    tu.right(y)
    tu.forward(x)
    tu.left(z)
    tu.forward(x)
    tu.left(y)
    tu.forward(x)
    # draw right top
    tu.right(y)
    tu.forward(x)
    tu.right(y)
    tu.forward(x)
    tu.left(z)
    tu.forward(x)
    tu.left(y)
    #draw left bottom
    tu.forward(2*x)
    tu.right(y)
    tu.forward(x)
    tu.left(z)
    tu.forward(x)
    tu.left(y)
    tu.forward(x)


def drawcircle(radius,j):
    tu.pensize(5)
    penList = ['yellow']
    for i in range(5):
        tu.pencolor(penList[i%1])
        tu.circle(radius)
        radius = radius - 10;

#function to draw circles inside swastika
def drawColor():
    val=150
    rad=30
    tu.pencolor('#FF007B')
    tu.penup()
    tu.setpos(val,val)
    tu.pendown()
    tu.fillcolor('#F7F3CE')
    tu.begin_fill()
    tu.circle(rad)
    tu.end_fill()
    tu.penup()
    tu.setpos(val,-val)
    tu.pendown()
    tu.begin_fill()
    tu.circle(rad)
    tu.end_fill()
    tu.penup()
    tu.setpos(-val,val)
    tu.pendown()
    tu.begin_fill()
    tu.circle(rad)
    tu.end_fill()
    tu.penup()
    tu.setpos(-val,-val)
    tu.pendown()
    tu.begin_fill()
    tu.circle(rad)
    tu.end_fill()
    tu.penup()


#starting function
def drawDesign():
    drawSwastika()
    drawColor()
    tu.setpos(0,0)
    tu.pendown()
    for i in range(10):
        drawcircle(150,i)
        tu.right(36)



drawDesign()
tu.done()
