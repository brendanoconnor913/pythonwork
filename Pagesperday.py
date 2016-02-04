

# Ask for how many Pages
# Ask for how many weeks
# How many days/week are you going to read.

# Calculate total days
# Calculate pages per day

#Output the result to the user.

pages = int(input("How many pages do you have to read: "))
weeks = int(input("How many weeks do you have in the semester: "))
daysperweek = int(input("How many days each week will you study: "))

totaldays = weeks * daysperweek
pageperday = pages / totaldays

print (pageperday)
