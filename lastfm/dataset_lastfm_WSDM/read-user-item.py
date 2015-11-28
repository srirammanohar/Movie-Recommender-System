import urllib
'''
with open('user-item.json') as data_file:
    print json.load(data_file)
'''
def parseFile(filename):
    for i in urllib.urlopen(filename):
        yield eval(i)
print "Reading"
data=list(parseFile("user-item.json"))
print data[0]