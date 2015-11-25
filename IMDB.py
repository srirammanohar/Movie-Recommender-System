__author__ = 'Rudra'
import csv
import urllib2

import urllib
import json
import demjson

a=[]
with open('ml-20m/links.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a.append(row)
set=[]
for l in a:
    if l['imdbId'] not in set:
        set.append(l['imdbId'])
i=0
#print len(set)
for i in range(len(set)):
    j="http://www.omdbapi.com/?i=tt"+str(set[i])+"&plot=short&r=json"
    try:
        response = urllib.urlopen(j)
        the_page = response.read().decode('utf-8')
        data = json.loads(the_page)
	with open('imdbinfo.json', 'a') as outfile:
		json.dump(data, outfile)
		outfile.write("\n")
    except:
        print i, "whoops error!"
        continue
#print type(data)
