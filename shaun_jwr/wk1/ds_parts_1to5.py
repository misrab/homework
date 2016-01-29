import csv
with open('drinks.csv', 'rb') as csvfile:
    all_rows = csv.reader(csvfile, delimiter=',', quotechar='|')
    index = 0
    data = []
    header = None
    for row in all_rows:
            if index == 0:
                header = row
            else:
                data.append(row)
            index += 1

# number one

print header
print data

# number two

beers = [d[1] for d in data]
# all first variable (number of beers) in each row, for all rows

print "beers = ", (beers)
print "len(beers) = ", len(beers)

# number three

dataNA = [float(d[1]) for d in data if d[-1] == "NA"]
print "List of NA beers", dataNA
print "len data(NA) = ", len(dataNA)

dataEU = [float(d[1]) for d in data if d[-1] == "EU"]
print "List of EU beers", dataEU
print "len(DATAEU) = ", len(dataEU)

# number four

aveNA = sum(dataNA)/len(dataNA)
print "Average NA", (aveNA)
print "Average NA to 2dp", ("{0:.2f}".format(aveNA))
# This above is rounding off to 2 figures

aveEU = sum(dataEU)/len(dataEU)
print "Average EU", (aveEU)
print "Average EU to 2dp", ("{0:.2f}".format(aveEU))

# number five

avebeer = [['continent, avg_beer'], ['EU', aveEU], ['NA', aveNA]]
length = len(avebeer[0])

with open('avg_beer.csv', 'wb') as testfile:
    csv_writer = csv.writer(testfile)
    for y in range(length):
        csv_writer.writerow([x[y] for x in avebeer])
