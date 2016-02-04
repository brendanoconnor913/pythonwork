########################################################################
##
## CS 101
## Program 6
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com
## Created 11/8/15
## Due 11/8/15
##
## PROBLEM : To take a ppm (P3) file input and filter the image down to 
## basic colors.
##
## ALGORITHM :
##  while True:
##      Display menu offering options for user "1 - Reduce Color PPM Q - Quit"
##      menuInput = input from user
##      if menuInput == "1":
##          while True:
##              fileName = file name user inputs
##              try:
##                  picFile = open(fileName)
##                  if not (header contains "P3" and color depth is 225):
##                      ouptput invalid file (need P3)
##                       continue
##              except:
##                  Output error statement
##                  continue
##
##              while True:
##                  outputFile = filename to output 
##                  try:
##                      open for writing outputFile
##                      break
##                  except:
##                      output error statement
##                      continue
##
##          break
##      elif menuInput == "Q":
##          break from loop and end program
##      else:
##          output invalid input statement
##          continue
##  
##  redCord = {'r':255, 'g':0, 'b':0}
##  grnCord = {'r':0, 'g':255, 'b':0}
##  blueCord = {'r':0, 'g':0, 'b':255}
##  blckCord = {'r':0, 'g':0, 'b': 0}
##  whtCord = {'r':255, 'g':255, 'b':255}
##  clrCordLst = [redCord, grnCord, blueCord, blckCord, whtCord]
##
##
##  cords = {}
##  i = 1
##  for line in picFile:
##     if line is a header line:
##         print(line, file = outputFile)
##     else:   
##          if i == 1:
##             cords['r'] = line
##             i += 1
##          if i == 2:
##             cords['g'] = line
##             i += 1
##     else:
##         cords['b'] = line
##         i = 1
##
##         minDist = 445 (~ max distantce it can be from a point)
##         newclr = {}
##
##         for point in clrCordLst:
##              dst = (cords['r']-point['r'])**2 + (cords['g']-point['g'])**2 \
##                  + (cords['b']-point['b'])**2
##              dst = dst**(1/2)
##
##              if dst < minDst:
##                  minDst = dst
##                  newclr = {'r':point['r'], 'g':point['g'], 'b':point['b']}
##      
##          print(newclr['r'], file = outputFile)
##          print(newclr['g'], file = outputFile)
##          print(newclr['b'], file = outputFile)
##
##
##  Close the input and output files
##
## ERROR HANDLING:
##      Error handling the input for file names and making sure the files open
##      
## OTHER COMMENTS:
##
##
########################################################################

#  Define dictionaries for use in calculating distance from colors
redCord = {'r':255, 'g':0, 'b':0}
grnCord = {'r':0, 'g':255, 'b':0}
blueCord = {'r':0, 'g':0, 'b':255}
blckCord = {'r':0, 'g':0, 'b': 0}
whtCord = {'r':255, 'g':255, 'b':255}
clrCordLst = [redCord, grnCord, blueCord, blckCord, whtCord]

def get_pic():
    """ Gets a ppm file of p3 type and 255 color depth
    Parameters: None
    Returns: picture - ppm file
    """
    while True:
        #  Get file name and open it
        fileName = input("Give the file name: ").lower()
        
        try:
            picture = open(fileName, 'r')
            
        except IOError:
            print("File name not found,try again.")
            continue

        # Verify that the file is P3 and 255 color depth
        ppmType = picture.readline().strip()
        picture.readline()
        clrDepth = picture.readline().strip()
        picture.close()
        if ppmType == "P3" and clrDepth == "255":
            return fileName
        else:
            print("File must be P3 .ppm type and 225 color depth.")
            continue

def get_oput():
    """ Obtains a file for outputting from the user.
    Parameters: None
    Returns: outputFile - file for altered picture
    """
    while True:
        oFileName = input("Name of file for outputting: ")
        try:
            outputFile = open(oFileName, 'w')
            return outputFile
        except IOError:
            print("The file name didn't work... Try another.")
            continue

def menu():
    """ Prints out the menu of options for user then executes the option
    Parameters: None
    Returns: pictureFile - value of "None" if user is quitting
             outpt - file new picture will be outputted to
    """
    while True:
        print(""" Menu Options
    1. Reduce Color PPM file
    Q. Quit""")

        #  Get user option
        menuInput = input("your choice: ").lower()

        #  Execute the option the user chose
        if menuInput == "1":
            #  Get the file the user wants to reduce
            pictureFile = get_pic()
            outpt = get_oput()
            return pictureFile, outpt

        #  End program if quit
        elif menuInput == "q":
            pictureFile = "quit"
            return pictureFile, None

        #  Didn't input a menu option
        else:
            print("Invalid input please enter one of the options given.")
            continue

def dist_calc(pt1a, pt1b, pt2a, pt2b, pt3a, pt3b):
    """ Takes 6 coordinate values and calculates the distance
    between two points in 3d space
    Parameters:  variables of the two points(pt1a, pt2a, pt3a) (pt1b, pt2b, pt3b)
    Returns: the 3d distance between the two points
    """
    dst = (pt1a-pt1b)**2 + (pt2a-pt2b)**2 + (pt3a-pt3b)**2
    dst = dst ** (1/2)
    return dst






def clr_reduc(pic, oputFile):
    """ takes a picture file and output file and outputs a color reduced picture
    Parameters: pic - the picture file
                oputFile - the file we will output the new image to
    returns: None
    """
    i = 1

    if not pic == "quit":
        picOpen = open(pic,'r')

        #  Need to discard the header lines
        print(picOpen.readline(), file = oputFile)
        print(picOpen.readline(), file = oputFile)
        print(picOpen.readline(), file = oputFile)

        #  Iterate through each line and save the value in a dict
        for line in picOpen:
            
            #  Put the rgb values in the variables a1,a2,a3 and use it to calc distances
            if i == 1:
                a1 = int(line.strip())
                i += 1
            elif i == 2:
                a2 = int(line.strip())
                i += 1
            elif i == 3:
                a3 = int(line.strip())
                i = 1
                minDist  = 445  # Max distance a point can be
                newclr   = {}
                k        = 0

                #  Compare the point in 3d space to the basic colors and choose the
                #  color that is the shortest distance away
                while k < len(clrCordLst):
                    d = dist_calc(a1, clrCordLst[k]['r'], a2, clrCordLst[k]['g'], \
                        a3, clrCordLst[k]['b'])

                    if d < minDist:
                        minDist = d
                        newclr = {'r':clrCordLst[k]['r'], 'g':clrCordLst[k]['g'], \
                         'b':clrCordLst[k]['b']}
                    k += 1

                #  Put the new point in the file
                print(newclr['r'], file = oputFile)
                print(newclr['g'], file = oputFile)
                print(newclr['b'], file = oputFile)

        
# Call the menu
pic1, output1 = menu()

# Use picture file for color reduction
clr_reduc(pic1, output1)

# Close your file
if not output1 == None:
    output1.close()
