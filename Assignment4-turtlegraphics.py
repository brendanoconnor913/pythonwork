########################################################################
##
## CS 101
## Program 4
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com
## Created 10/18/2015
## Due 10/18/2015
##
## PROBLEM : We are creating a user interface to the turtle python graphics library.
##
## ALGORITHM :
## set turtledrawing = True
## while turtledrawing:
##        while True:
##             get filename from user
##             if filename == "quit"
##                break from loop and end program
##             try to open filename given and assign it to variable turtlefile
##             except output invalid file error
##
##        for line in turtlefile
##            if filename == "quit":
##                turtledrawing = False
##                break
##
##            gencommand = list of each word in line
##            try
##                scommand = first entry of gencommand list
##                if scommand in list of valid commands
##                    if scommand = "color"
##                        try
##                            set drawclr = fillclr = second entry of gencommand
##                            return None
##                        except
##                            output line and invalid param error statement
##
##                    elif scommand = "rect"
##                        try
##                            set x,y,width,height = 2nd,3rd,4th,5th entry of gencommand
##                            pick pen up and set at (x,y), turn tutle to face +x
##                            draw in drawclr and fillclr a rectangle to the right and down of size width by height
##
##                        except
##                            output line and invalid param error statement
##
##                    elif scommand = "circle"
##                        try
##                            set x, y, radius = 2nd, 3rd, 4th entry of gencommand
##                            pick pen up and set at (x,y) and draw with drawclr and fillclr a circle radius*2 wide
##                        except
##                            output line and invalid param error statement
##
##                    else ("line")
##                        try
##                            set x, y, heading, length = 2nd, 3rd, 4th, 5th entry of gencommand
##                            pick pen up and set at (x,y) in direction heading for length
##                        except
##                            output line and invalid param error statement
##
##                else
##                    output not a defined command error
##            except
##                output line and invalid command (no command was entered so index error)
##         continue to beginning of the start of the first while loop and ask for filename as input
##
##
##
##
## ERROR HANDLING:
##      Error for file names and for each command and parameters within the turle file
##
## OTHER COMMENTS:
##
##
########################################################################

# 1. Think before you program
# 2. A program is a human readable essay on problem solving that is excuted by a computer
# 3. Best way to improve is to practice
# 4. Foolish consistency is the hobgoblin of little minds
# 5. Test your code constantly and thoroughly
# 6. If it's hard to write, its hard to read, add a comment.
# 7. All input is evil until proven other wise

import turtle

# For checking the commands in the turtle file
valcommands = ['rect', 'color', 'line', 'circle']

# Initializing variables and setting them to a default value
clr = 'black'
turtle.pencolor(clr)
turtle.fillcolor(clr)
turtle.speed(10)
turtlefile = ""

def draw_rectangle(x,y,width,height):
    """
    Draws a rectangle with the upper left hand corner starting at point (x,y).
    The said rectangle has the dimensions width x height.
    :param x:
    :param y:
    :param width:
    :param height:
    :return: None
    """
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.setheading(0)  # Set heading in x+ direction
    turtle.begin_fill()
    turtle.begin_poly()
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.right(90)
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.end_poly()
    turtle.end_fill()
    return None

def draw_line(x,y,heading,length):
    """
    A function that draws a line start at point (x,y) in the direction param:heading
    for distance param:length.
    :param x:
    :param y:
    :param heading:
    :param length:
    :return: None
    """
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(heading)
    turtle.forward(length)
    return None

def draw_circle(x,y,radius):
    """
    A function that draws a circle centered at point (x,y) with a radius="param radius:
    :param x:
    :param y:
    :param radius:
    :return:None
    """
    turtle.penup()
    turtle.setx(x+radius)
    turtle.sety(y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
    return None

def set_color(clr):
    """
    A function that sets the pen and fill color to :param clr:
    :param clr:
    :return: None
    """
    turtle.pencolor(clr)
    turtle.fillcolor(clr)
    return None

turtledrawing = True
while turtledrawing:

    # Get the file name from the user and open file for reading
    while True:
         filename = input("Please give the name of the file you want to draw: ").lower()
         turtle.clear()  # Clear any previous drawings (if there are any)
         if "quit" == filename:  # For the user to exit the program
             turtledrawing = False
             break
         try:
             turtlefile = open(filename, 'r')
             break
         except:
            print("The name of the file was invalid. Please try again...")
            continue

    # Iterate through each line of the file and execute the given commands
    for line in turtlefile:

        # Don't execute the code if the user enters quit
        if filename == "quit":
            break

        commandline = line.split()
        try:

            # Assign the command to a variable and check to see it is valid
            command = commandline[0].lower()
            if command in valcommands:

                # Since line is valid check to see which command it is and execute the command
                if command == "color":
                    try:
                        clr = commandline[1]
                        set_color(clr)
                    except IndexError:
                        print(line)
                        print("This line contained an error: Not enough arguments were given for the\
                         color command (1 needed)")
                        continue

                elif command == "rect":
                    try:
                        x, y, width, height = int(commandline[1]), int(commandline[2]), int(commandline[3]), int(commandline[4])
                        draw_rectangle(x, y, width, height)
                    except IndexError:
                        print(line)
                        print("This line contained an error: Not enough arguments were \
                         given for the rect command (4 needed)")
                        continue
                    except ValueError:
                        print(line)
                        print("You entered invalid input in this line")
                        continue

                elif command == "circle":
                    try:
                        x, y, radius = int(commandline[1]), int(commandline[2]), int(commandline[3])
                        draw_circle(x, y, radius)
                    except IndexError:
                        print(line)
                        print("This line contained an error: Not enough arguments were given for\
                         the circle command (3 needed)")
                        continue
                    except ValueError:
                        print(line)
                        print("You entered invalid input in this line")
                        continue

                else:  # command == "line"
                    try:
                        x, y, heading, length = int(commandline[1]), int(commandline[2]), int(commandline[3]), int(commandline[4])
                        draw_line(x, y, heading, length)
                    except IndexError:
                        print(line)
                        print("This line contained an error: Not enough arguments were given\
                         for the line command (4 needed)")
                        continue
                    except ValueError:
                        print(line)
                        print("You entered invalid input in this line")
                        continue

            # The first entry of the commandline wasn't found in the valid commands
            else:
                print("This line was blank (no command)")
                continue

        # First entry of command line was empty result in an index error
        except IndexError:
            print(line)
            print("No command was found for this line")
            continue



# Code will finish the for loop after each line has be iterated over then return to the top of the loop
# Then it will ask for a new file name to execute. This will continue until "quit" is entered.