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

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  darty.penup()
  darty.goto(-1, -1)
  darty.pendown()
  for i in [1, 1, 1, 1]:
    darty.forward(2)
    darty.left(90)

def drawLine(myturtle, x_start=0, y_start=0, x_end=0, y_end=0):
  darty.penup()
  darty.goto(x_start,y_start)
  darty.pendown()
  darty.goto(x_end, y_end)

def drawCircle(myturtle=None, radius=0):
  darty.goto(0,-1)
  darty.circle(radius)

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  distance = darty.distance(0,0)
  if distance > 1:
    darty.dot(2, "red")
    return False
  else:
    darty.dot(2, "green")
    return True
  
def setUpDartboard(window=None, myturtle=None):
  darty = turtle.Turtle()
  wn= turtle.Screen()
  wn.mode('world')
  turtle.setworldcoordinates(-1, -1, 2.5, 2.5)
  drawSquare(darty, 2, -1, 1)
  drawLine(darty, -1, 0, 1, 0)
  drawLine(darty, 0, -1, 0, 1)
  drawCircle(darty, 1)
    
def throwDart(myturtle=None):
  x_coord= random.uniform(-1, 1)
  y_coord= random.uniform(-1, 1)
  darty.penup()
  darty.goto(x_coord, y_coord)
  darty.dot(2, "blue")

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
  elif p1point == p2point:
    print("the game ended in a tie!")
  else:
    print("player two wins!")

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
    darty = turtle.Turtle()
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
