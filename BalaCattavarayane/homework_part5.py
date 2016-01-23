import csv

output = [['continent', 'avg_beer'], ['NA', '145.43'], ['EU', '193.78']]

with open('avg_beer.csv', 'wb') as outFile:
    csv.writer(outFile).writerows(output)

# PART 5 solution
print '<< PART 5 solution >>'
print 'File created successfully'
