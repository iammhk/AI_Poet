import csv

with open('sher fazli.csv',encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[2]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    #print(colors)

    # now, remember our lists?

    #whatColor = input('What color do you wish to know the date of?:')
    #coldex = colors.index(whatColor)
    #theDate = dates[coldex]
    #print('The date of',whatColor,'is:',theDate)