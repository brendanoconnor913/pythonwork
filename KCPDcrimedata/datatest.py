import csv 

#  Open file and convert to csv
dataFile = open('incidents.csv', 'r')
cdataFile = csv.reader(dataFile)

#  Add the zips as keys to dictonaries and total the number of times it appears
zipcount = {}
for line in cdataFile:
    if line[4] == '' or line[4] == '0':
        zipcount['99999'] = zipcount.get('99999', 0) + 1
    else:
        zipcount[line[4]] = zipcount.get(line[4], 0) + 1

#  Remove the header then sort the list by zip
zipcount.pop('Zip Code')
zorder = sorted(zipcount.keys())

#  Output data in formatted table
print("{:<15s} {:<15s}".format("Zip Code", "Crimes"))
print("=" * 25)
for key in zorder:
    print("{:<15} {:^10}".format(key, zipcount[key]))

dataFile.close()

