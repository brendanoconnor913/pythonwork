########################################################################
##
## CS 101
## Program 5
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com
## Created 11/1/2015
## Due 11/1/2015
##
## PROBLEM : We are taking data on rainfall for each day and processing it to display the total
##              rainfall each month for each year along with the average rainfall for each month.
##              Finally we will output this formatted information to a new file.
##
## ALGORITHM :
##  Get input from the user requesting the name of the csv file we will be using for input
##  Try: 
##      open the file and assign it to variable "wdatafile"
##  Except: 
##      output error message: file can't be found
##
##  Get input from user on a file to output the data to
##  Try:
##      open a new file for writing and assign to variable outputFile
##  Except:
##      output io error message
##
##  for line in wdatafile:
##      seperate each line on ',' then remove any white spaces and insert into list "rawData"
##  
##  i = 0
##  procData = []
##  while i < len(rawData)-1:
##      date = [rawData[i][0:4],rawData[i][4,6],rawData[i][6:]]
##      procData.append((date,rawData[i+1]))
##      i += 2
##  
##  Note: Each entry should be in the form [([year,month,day], precipitation), ...]
##
##  for entry,i in enumerate(procData):
##      if entry[2] == 'NA':
##          procData.pop(i)
##  
##  byMonthAve = []
##  for year in ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009']:
##      for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
##          byMonthAve.append(year+month)
##          precpSum = []
##          for entry in procData:
##              if entry[0][0] == year and entry[0][1] == month:
##                  precpSum.append(float(int(entry[1]))
##          monthAve = precpSum.sum() / len(precpSum)
##          byMonthAve.append(monthAve)
##  
##  totalMonthAve = []
##  for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
##      totalMonthAve.append(month)
##      precpSum = []
##      for entry in procData:
##          if entry[0][1] == month:
##              precpSum.append(float(int(entry[1]))
##      tMonthAve = precpSum.sum() / len(precpSum)
##      totalMonthAve.append(tMonthAve)
##  
##  Output both byMonthAve and totalMonthAve to outputFile
##
##  Close both files
##
## ERROR HANDLING:
##      Error handling for inputting file names and outputting file names.
##
## OTHER COMMENTS:
##
##
########################################################################

# 1. Think before you program
# 2. A program is a human readable essay on problem solving that is executed by a computer
# 3. Best way to improve is to pratice
# 4. Foolish consistency is the hobgoblin of little minds
# 5. Test your code thoroughly and often
# 6. If it was hard to write, it is hard to read, add a comment
# 7. All input is evil until proven otherwise

import csv

def get_file():
    """ Obtains the name of the data file to be used for calculating month averages
        Parameters: None
        returns : csvFile - the open file
    """
    while True:
        try:
            tFile   = input("Please enter the csv file for processing: ")
            csvFile = open(tFile, 'r')
            return csvFile
        except IOError:
            print("File couldn't be found please try again")
            continue


def get_oput_file():
    """ Obtains the name of the data file to outfile information
        Parameters: None
        returns : outFile - the file to be created
    """
    while True:
        try:
            tFile = input("Please enter the monthly data file to save to: ")
            if tFile[-4:] != ".csv":
                print("Please give a file ending in .csv")
                continue
            outFile = open(tFile, 'w')
            return outFile
        except IOError:
            print("IO error, please try again.")
            continue

def data_format(csvFile):
    """Takes csvFile and inserts each entry into a list
    of the format [([year,month,day], precipitation)]
    Parameters:
        csvFile - csvFile opened with csv.reader()
    returns: 
        a list containing each entry formatted
    """
    procData = []
    for k in csvFile:
        date = [k[0][0:4],k[0][4:6],k[0][6:]]
        if k[1] != 'NA':
            procData.append((date,float(k[1])))
    return procData

def year(line):
    """ Function cleans up code for getting the year of an entry
    Parameters: line - an entry in a list that has been outputted by data_format (a formatted list)
    returns: the year of the given line
    """
    return line[0][0]

def month(line):
    """ Function cleans up code for getting the month of an entry
    Parameters: line - an entry in a list that has been outputted by data_format (a formatted list)
    returns: the month of the given line
    """
    return line[0][1]

def day(line):
    """ Function cleans up code for getting the day of an entry
    Parameters: line - an entry in a list that has been outputted by data_format (a formatted list)
    returns: the day of the given line
    """
    return line[0][2]

def precp(line):
    """ Function cleans up code for getting the precipitation of an entry
    Parameters: line - an entry in a list that has been outputted by data_format (a formatted list)
    returns: the precipitation of the given line
    """
    return line[1]

def by_month_total(yearLst, monthLst, pDataLst):
    """ takes a lists of years and months in data and formatted data 
    (output from data_format) and gives a list of the total precipitation
    for each month in each year
    Parameters:
        yearLst - list containing every year in data
        monthLst - list containing every month in data
        pDataLst - formatted data list from data_format

    """
    byMonthTotal = []
    for y in yearLst:
        for m in monthLst:
            byMonthTotal.append(y+m)
            precpSum = []
            for line in pDataLst:
                if year(line) == y and month(line) == m:
                    precpSum.append(precp(line))
            total = sum(precpSum)
            byMonthTotal.append(total)
    return byMonthTotal

def total_month_ave(yearLst, monthLst, pDataLst):
    """Takes the yearLst, monthLst, and pDataLst and returns the average
     of each month total
     Parameters:
        yearLst - a list containing all of the years in the data
        monthLst - a list containing all of the months in the data
        pDataLst - the data formatted from data_format
    returns:
        totalMonthAve - a list of each month and the average of the totals from
        each month

    """
    totalMonthAve = []
    for m in monthLst:
        totalMonthAve.append(m)
        precpSum = []
        for line in pDataLst:
            if month(line) == m:
                precpSum.append(precp(line))
        tMonthAve = sum(precpSum) / len(yearLst)
        totalMonthAve.append(tMonthAve)
    return totalMonthAve

def ave_month_oput(amt):
    """Formats the output for the average month total
    Parameters:
        amt - the output from total_month_ave()
    returns:
        the data from amt formatted

    """
    print("{:^20s}".format("Monthly Total Averages"))
    print("{:<10s} {:>10s}".format("Month","Avg Precip"))
    print("="*21)
    i = 0
    while i <= len(amt)-1:
        if amt[i]   == "01":
            strmonth    = "Jan"
        elif amt[i] == "02":
            strmonth    = "Feb"
        elif amt[i] == "03":
            strmonth    = "March"
        elif amt[i] == "04":
            strmonth    = "Apr"
        elif amt[i] == "05":
            strmonth    = "May"
        elif amt[i] == "06":
            strmonth    = "Jun"
        elif amt[i] == "07":
            strmonth    = "Jul"
        elif amt[i] == "08":
            strmonth    = "Aug"
        elif amt[i] == "09":
            strmonth    = "Sep"
        elif amt[i] == "10":
            strmonth    = "Oct"
        elif amt[i] == "11":
            strmonth    = "Nov"
        elif amt[i] == "12":
            strmonth    = "Dec"
        print("{:<10s} {:>10.4f}".format(strmonth,amt[i+1]))
        i += 2

def month_total_oput(byMonthTotal, oputFile):
    """ outputs the data from by_month_total to the outputFile
    Parameters:
        byMonthTotal - list of data from by_month_total
        oputFile - file to output data
    returns:
        None
    """
    i = 0
    while i <= len(byMonthTotal)-1:
        print(byMonthTotal[i]+","+str(byMonthTotal[i+1]), file=oputFile)
        i += 2

# Get input and output file names from user
dataFile    = get_file()
dataOutFile = get_oput_file()

# Format the data input
rawData     = csv.reader(dataFile)
procData    = data_format(rawData)

# Make a list of months and years in data to for iteration
years   = []
months  = []
for line in procData:
    if not year(line)   in years:
        years.append(year(line))
    if not month(line)  in months:
        months.append(month(line))

# Take the years list, months list, and data and get the total precpitation 
# by each month of each year
byMonthTotal    = by_month_total(years, months, procData)

# Take the years list, months list, and data and get the average of
# each month total
aveMonthTotal   = total_month_ave(years,months, procData)

# Output the data
ave_month_oput(aveMonthTotal)
month_total_oput(byMonthTotal, dataOutFile)

# Close both of the files
dataFile.close()
dataOutFile.close()