

daysCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]

dayIndex = 0
count = 0

for year in range(1901, 2001):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        daysCount[1] = 29
    else:
        daysCount[1] = 28


    for month in enumerate(daysCount):

        if (dayIndex+1) % 7 == 6:
            print days[(dayIndex+1)%7], year, months[month[0]] , "1st"
            count += 1

        dayIndex += month[1]



print "Count:", count
