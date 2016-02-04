########################################################################
##
## CS 101
## Program 7
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com
## Created 11/21/15
## Due 11/22/15
##
## PROBLEM : Taking data from the KCPD open data and providing an anlaysis
##      and presenting the final data in a formatted display.
##
## ALGORITHM :
##     import csv
##
##     def menu_input():
##          while True
##              userInput = input("==> ")
##              if userInput == "1" or userInput == "2":
##                      return userInput
##              elif userInput.lower() == "q":
##                      return False
##              else:
##                      print("Invalid input choose from the folowing:1,2,q.")
##                      continue   
##
##     def zip_sum():
##          dataFile = open('incidents.csv', 'r')
##          cdataFile = csv.reader(dataFile)
##          zipcount = {}
##          for line in cdataFile:
##              if line[4] == '' or line[4] == '0':
##              zipcount['99999'] = zipcount.get('99999', 0) + 1
##          else:
##              zipcount[line[4]] = zipcount.get(line[4], 0) + 1
##
##          zipcount.pop('Zip Code')
##          zorder = sorted(zipcount.keys())
##
##          print("{:<15s} {:<15s}".format("Zip Code", "Crimes"))
##          print("=" * 25)
##          for key in zorder:
##              print("{:<15} {:^10}".format(key, zipcount[key]))
##
##          dataFile.close()
##
##     def vic_count():
##          while True:
##              try:
##                  detailFile      = open('details.csv', 'r')
##                  incidentFile    = open('incidents.csv', 'r')
##                  offensesFile    = open('offenses.csv', 'r')
##                  break
##              except IOError:
##                  print("Error opening files, try again.")
##                  continue
##
##          cdetailFile     = csv.reader(detailFile)
##          cincidentFile   = csv.reader(incidentFile)
##          coffensesFile   = csv.reader(offensesFile)
##
##          vicPerOff       = {} # offense description  : # of victims
##          offNumPerVic    = {} # offense #            : # of victims
##          vicPerReport    = {} # report num           : # of victims
##          offForReport    = {} # report num           : offense #
##          offensenum      = {} # offense #            : offense description
##
##          #  Get the offensenum dict set up
##          for line in coffensesFile:
##              offensenum[line[0]] = line[1]
##              offensenum.pop('Offense')  # Remove the header
##
##          #  Get offForReport populated
##          for line in cincidentFile:
##              offForReport[line[0]] = line[3]
##              offForReport.pop('Report_No') # Remove the header
##
##          #  Get vicPerReport populated
##          for line in cdetailFile:
##              if line[1] == "VIC":
##              vicPerReport[line[0]] = vicPerReport.get(line[0], 0) + 1
##
##          #  Get offNumPerVic populated
##          for key in offForReport:
##              if key in vicPerReport:
##                  offNumPerVic[offForReport[key]] = offNumPerVic.get(offForReport[key], 0) + vicPerReport[key]
##
##          #  Get final dict we need for data report
##          for key in offNumPerVic:
##              vicPerOff[offensenum[key]] = offNumPerVic[key]
##
##          #  Output data in descending from # of victims  
##          print("{:<22} {:>15}".format("Offense", "Victims"))
##          print("="*38)
##          for k in sorted(vicPerOff,key=vicPerOff.get,reverse=True):
##              print("{:<22} {:>15}".format(k, vicPerOff[k]))
##
##          detailFile.close()
##          incidentFile.close()
##          offensesFile.close()
##            
##     def menu():
##         print("{:^50s}".format("KCPD Crime Statistics"))
##         print("1. Summary by Zip Code")
##         print("2. Victime count by offense Type")
##         print("3. Quit")
##         response = menu_input()
##         if response == "1":
##              zip_sum()
##              return True
##         elif response == "2":
##              vic_count()
##              return True
##         else:
##              return False
##     
##      while running:
##          running = menu()
##          
##
## ERROR HANDLING:
##      Error handling the files being opened and user input on menu options
##      Will not cover incorrectly named files
##      
## OTHER COMMENTS:
##
##
########################################################################

#  1. Think before you program
#  2. A program is a human readable essay on problem solving executed by a computer
#  3. Best way to improve is to practice
#  4. Foolish consistency is the hobgoblin of little minds
#  5. Test your code thoroughly and often
#  6. If it was hard to write it is hard to read, add a comment
#  7. All input is evil until proven otherwise

import csv

def menu_input():
    """ Get input from user, execute menu options if 1 or 2
    end program if q and ask again if not those 3 options
    Input: None
    Return: userInput - menu option or Flase to end program

    """
    while True:
        userInput    = input("==> ")
        if userInput == "1" or userInput == "2":
            return userInput
        elif userInput.lower() == "q":
            return False
        else:
            print("Invalid input choose from the folowing:1,2,q.")
            continue   

def zip_sum():
    """ takes the data file incidents.csv and presents a count of the number
    of offenses per zip code ordered by zip

    Input: None
    Returns: None
    """
    #  Open the file needed for this report and process w/ csv module
    dataFile    = open('incidents.csv', 'r')
    cdataFile   = csv.reader(dataFile)

    #  Create a library to store data and iterate through set to 
    #  count the number of incidents per zip
    zipcount    = {}
    for line in cdataFile:
        if line[4] == '' or line[4] == '0':
            zipcount['99999'] = zipcount.get('99999', 0) + 1
        else:
            zipcount[line[4]] = zipcount.get(line[4], 0) + 1

    zipcount.pop('Zip Code')  #  Remove the header
    zorder = sorted(zipcount.keys()) #  Sort the keys for output

    #  Output number of crimes ordered by zip
    print("{:<15s} {:<15s}".format("Zip Code", "Crimes"))
    print("=" * 25)
    for key in zorder:
        print("{:<15} {:^10}".format(key, zipcount[key]))

    #  Close the file used for the report
    dataFile.close()

def vic_count():
    """Takes details.csv, incidents.csv, and offenses.csv and presents
    data of the number of incidents for each type of offense ordered
    in descending order by number of incidents.

    Input: None
    Returns: None
    """
    #  Open all of the files necessary for report
    while True:
        try:
            detailFile      = open('details.csv', 'r')
            incidentFile    = open('incidents.csv', 'r')
            offensesFile    = open('offenses.csv', 'r')
            break
        except IOError:
            print("Error opening files, try again.")
            continue

    #  Process files with csv module
    cdetailFile     = csv.reader(detailFile)
    cincidentFile   = csv.reader(incidentFile)
    coffensesFile   = csv.reader(offensesFile)

    #  Set up all of the dictionaries we will need to store and 
    #  manipulate all of the data to get the report in the final format
    vicPerOff       = {} # offense description  : # of victims
    offNumPerVic    = {} # offense #            : # of victims
    vicPerReport    = {} # report num           : # of victims
    offForReport    = {} # report num           : offense #
    offensenum      = {} # offense #            : offense description

    #  Get the offensenum dict set up
    for line in coffensesFile:
        offensenum[line[0]] = line[1]
    offensenum.pop('Offense')  # Remove the header

    #  Get offForReport populated
    for line in cincidentFile:
        offForReport[line[0]] = line[3]
    offForReport.pop('Report_No') # Remove the header

    #  Get vicPerReport populated
    for line in cdetailFile:
        if line[1] == "VIC":
            vicPerReport[line[0]] = vicPerReport.get(line[0], 0) + 1

    #  Get offNumPerVic populated
    for key in offForReport:
        if key in vicPerReport:
            offNumPerVic[offForReport[key]] = offNumPerVic.get(offForReport[key], 0) + vicPerReport[key]

    #  Get final dict we need for data report
    for key in offNumPerVic:
        vicPerOff[offensenum[key]] = offNumPerVic[key]

    #  Output data in descending from # of victims  
    print("{:<22} {:>15}".format("Offense", "Victims"))
    print("="*38)
    for k in sorted(vicPerOff,key=vicPerOff.get,reverse=True):
        print("{:<22} {:>15}".format(k, vicPerOff[k]))

    #  Close all of the files we opened for this report
    detailFile.close()
    incidentFile.close()
    offensesFile.close()
            
def menu():
    #  Present menu options
    print("\n")
    print("{:^50s}".format("KCPD Crime Statistics"))
    print("1. Summary by Zip Code")
    print("2. Victime count by offense Type")
    print("Q. Quit")

    #  Get input
    response = menu_input()

    #  Execute functions corresponding to the input given
    if response == "1":
        zip_sum()
        return True
    elif response == "2":
        vic_count()
        return True
    else:
        return False
     
def main():
    running = True

    # Continue to execute menu until user inputs 'q'
    while running:
          running = menu()

main()
