from urllib.request import urlopen
from io import StringIO
import csv

def datal

datal = urlopen("http://www.sharecsv.com/s/c6ecf2e89c3b1472614295b4a647e4f6/GuatED.csv").read().decode('ascii','ignore')
datafile = StringIO(data)
csvReader = csv.reader(datafile)

if datal == '__main__':
    main()
    process.process()

