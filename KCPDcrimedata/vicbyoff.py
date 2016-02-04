import csv

while True:
    try:
        detailFile      = open('details.csv', 'r')
        incidentFile    = open('incidents.csv', 'r')
        offensesFile    = open('offenses.csv', 'r')
        break
    except IOError:
        print("Error opening files, try again.")
        continue

cdetailFile     = csv.reader(detailFile)
cincidentFile   = csv.reader(incidentFile)
coffensesFile   = csv.reader(offensesFile)

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

detailFile.close()
incidentFile.close()
offensesFile.close()
