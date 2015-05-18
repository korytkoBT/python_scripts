import collections
import csv 
import sys

plik = sys.argv[1]

listOfResults = []
with open(plik, 'r') as f:
    for row in csv.DictReader(f):
        listOfResults.append(row)

returnValues = collections.defaultdict(list)
for row in listOfResults:
    print row.keys()
    print row
    returnValues[row['student']].append(int(row['ocena']))

for k, v in returnValues.iteritems():
    print "Srednia studenta %s to %2.2f" % (k, float(sum(v))/len(v))

