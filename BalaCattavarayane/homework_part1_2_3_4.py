import csv

i=0
data = []
with open('.\\data\\drinks.csv', 'rU') as drinksFile:
    reader = csv.reader(drinksFile, delimiter=",", quotechar='|')    
    for row in reader:
        if i == 0 :
            header = row
        else:
            data.append(row)

        i += 1

# PART 1 solution
print '<< PART 1 solution >>'
print header
print data

beerServ = []
for dataRow in data:
    beerServ.append(dataRow[1])

print beerServ
print len(beerServ)

print '<< PART 2 solution >>'
# PART 2 solution
# use list comprehension
beers = [rowData[1] for rowData in data]
print beers
print len(beers)            

# PART 3 solution
print '<< PART 3 solution >>'
NA_beers = [int(rowData[1]) for rowData in data if rowData[5] == 'NA']
print NA_beers
print len(NA_beers)

EU_beers = [int(rowData[1]) for rowData in data if rowData[5] == 'EU']
print EU_beers
print len(EU_beers)

print '<< PART 4 solution >>'
# PART 4 solution     
naBeersAvg = round(float(sum(NA_beers)) / len(NA_beers), 2)
print naBeersAvg

euBeersAvg = round(float(sum(EU_beers)) / len(EU_beers), 2)
print euBeersAvg




