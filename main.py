'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time


#########################################################
#                   Your Code Goes Below                #
#########################################################
darty = turtle.Turtle()
printer = turtle.Turtle()


def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  darty.penup()
  darty.goto(-1, -1)
  darty.pendown()
  for i in [1, 1, 1, 1]:
    darty.forward(2)
    darty.left(90)
    
'''Takes a turtle value, width, top left x value and top left y value, and draws a square with these parameters'''

def drawLine(myturtle, x_start=0, y_start=0, x_end=0, y_end=0):
  darty.penup()
  darty.goto(x_start,y_start)
  darty.pendown()
  darty.goto(x_end, y_end)

'''takes arguements turtle, starting x and y position, and ending x and y position, and draws a line'''

def drawCircle(myturtle=None, radius=0):
    darty.goto(0,-radius)
    darty.circle(radius)

'''Takes a turtle and radius parameter and draws a Circle'''

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  distance = darty.distance(0,0)
  if distance > 1:
    darty.dot(2, "red")
    return False
  elif 0.4 < distance < 1 :
    darty.dot(2, "green")
    return True
  else:
    darty.shape("circle")
    darty.color("purple")
    darty.stamp()
    darty.shape("classic")
    darty.color("black")
    print("So close to the bullseye!")
    return True
    
'''takes a turtle, x and y values of the center of the circle, and a radius and returns either True or False depending on the placement of the dart'''

def printCount (start_x, start_y, myturtle=None):
  printer = turtle.Turtle()
  printer.goto(start_x, start_y)
  printer.write(("Player 1 Score: ", p1point), True, align=center)
  printer.goto(start_x, start_y + 5)
  printer.write(("Player 2 Score: ", p2point), True, align=center)

'''takes the turtle, a starting x value, and a starting y value and writes the players scores above the dartboard'''


def setUpDartboard(window=None, myturtle=None):
  darty = turtle.Turtle()
  wn= turtle.Screen()
  wn.mode('world')
  turtle.setworldcoordinates(-1, -1, 2.5, 2.5)
  drawSquare(darty, 2, -1, 1)
  drawLine(darty, -1, 0, 1, 0)
  drawLine(darty, 0, -1, 0, 1)
  drawCircle(darty, 1)
  drawCircle(darty, 0.4)

'''takes the arguments window type and turtle and draws a dartboard'''
    
def throwDart(myturtle=None):
  x_coord= random.uniform(-1, 1)
  y_coord= random.uniform(-1, 1)
  darty.penup()
  darty.goto(x_coord, y_coord)
  darty.dot(2, "blue")

'''takes a turtle argument and uses it to throw the darts at the dartboard'''

def playDarts(myturtle=None):
  p1point = 0
  p2point = 0
  for i in range(10):
    throwDart(darty)
    if isInCircle(darty,0,0,1):
      p1point = p1point + 1
    else:
      p1point = p1point
    throwDart(darty)
    if isInCircle(darty,0,0,1):
      p2point = p2point + 1
    else:
      p2point = p2point
  print("player 1 score:", p1point)
  print("player 2 score:", p2point)
  if p1point > p2point:
    print("player one wins!")
    drawStar(printer)
  elif p1point == p2point:
    print("the game ended in a tie!")
  else:
    print("player two wins!")
    drawStar(printer)
'''takes a turtle argument and plays a game of darts'''

def drawStar(myturtle=None):
  printer.goto(0,1)
  for i in ["pink", "blue", "yellow", "red", "purple"]:
    printer.color(i)
    printer.forward(3)
    printer.right(144)
    
'''takes a turtle argument and uses it to draw a star'''

def montePi(myturtle=None, number_darts=0):
  inside_count = 0
  for i in range(number_darts):
    throwDart(darty)
    if isInCircle(darty, 0,0,1):
      inside_count = inside_count + 1
    else:
      inside_count = inside_count
  approxpt1 = (inside_count / number_darts)
  approxofpi = approxpt1 * 4 
  return approxofpi

'''Takes a turtle argument and a number of darts and returns an approximation of pi'''

  
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty.speed(0)  # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)

    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(
        input(
            "\nPlease input the number of darts to be thrown in the simulation:  "
        ))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using " + str(number_darts) +
          " virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()


main()
