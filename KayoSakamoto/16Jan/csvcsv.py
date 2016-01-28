def mycsv(filename):
	import csv
	with open(filename, 'rb') as cf:
		myReader = csv.reader(cf, delimiter=' ', quotechar='|')
        myReader.next()