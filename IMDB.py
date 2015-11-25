__author__ = 'Rudra'
import csv
import urllib2
import urllib
import json

a=[]
with open('ml-20m/links.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a.append(row)
data=[]
set=[]
for l in a:
    if l['imdbId'] not in set:
        set.append(l['imdbId'])
i=0
for i in range(0,len(set)):
    print i
    j="http://www.omdbapi.com/?i=tt"+str(set[i])+"&plot=short&r=json"
    try:
        req = urllib2.Request(j)
        response = urllib2.urlopen(req)
        the_page = response.read()
        data.append(the_page)
    except urllib2.HTTPError as e:
        print i, "whoops error!"
        continue
print len(data)
print type(data[0])
with open('imdbinfo.json', 'w') as outfile:
    json.dump(data, outfile)
