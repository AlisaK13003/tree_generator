import turtle

def drawTree(t, c, f, r, x, y):
     # Set position for tree
     t.penup()
     t.setpos(x, y)
     t.left(90)
     t.pendown()
 
     # Draw trunk of the tree
     t.color("burlywood4")
     t.pensize(10)
     t.forward(40)
     t.pensize(1)

     # Draw leaves of the tree
     t.color(c)
     t.begin_fill()
     t.right(90)
     t.circle(45)
     t.end_fill()

     t.color(r)
     t.penup()
     t.setpos(x + 15, y + 60)
     t.pendown()

     diameter = 5
     z = 1
     n = 1
     while(z < 7):
          t.begin_fill()
          t.circle(diameter)
          t.left(n * 60)
          t.penup()
          t.forward(30)
          t.end_fill()
          t.pendown()
          z = z + 1

     t.color(f)
     t.penup()
     t.setpos(x + 10, y + 75)
     t.pendown()

     diameter = 3
     m = 1
     s = 1
     while(m <= 5):
          t.begin_fill()
          t.circle(diameter)
          t.left(s * 72)
          t.penup()
          t.forward(21)
          t.end_fill()
          t.pendown()
          m = m + 1



def main():
     dan = turtle.Turtle()
     dan.speed(60)
     answer = input ("Would you like to draw a tree (y/n)? ")

     while (answer == "y"):
          c = (input("What are the colors of the tree leaves? "))
          r = (input("What are the colors of the fruits? "))
          f = (input("What are the colors of the flowers? "))
          x = int(input("Enter the position of the tree on the x-axis: "))
          y = int(input("Enter the position of the tree on the y-axis: "))
          drawTree(dan, c, f, r, x, y)
          answer = input ("Would you like to draw a tree (y/n)? ")
     else:
          (answer == "n")

main()
