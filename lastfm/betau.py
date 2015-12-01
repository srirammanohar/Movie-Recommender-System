__author__ = 'sriram'
_author__ = 'sriram'
__author__ = 'sriram'
__author__ = 'sriram'
__author__ = 'sriram'
import gzip
from collections import defaultdict
import math
import numpy
import operator
#import nltk
import random

def readGz(f):
  for l in gzip.open(f):
    yield eval(l)
itemCount = defaultdict(int)
totalPurchases = 0
alphac = 0.0
alphap = 0.0

allRatings = []
userRatings = defaultdict(list)
itemRatings = defaultdict(list)

ur = []
ir = []
count = 0
uiRatings = {}
uiRatingsv = {}
uiRatingsTotal = 0
userlist = []
itemlist = []
iteration = 0
for l in open("user_rating.dat"):
  if l.startswith("userID"):
      continue
  u,i,rat = l.strip().split()
  if(u not in userlist):
      userlist.append(u)
  if(i not in itemlist):
      itemlist.append(i)
print userlist
print itemlist
print "I am Sriram . I suck"


#for l in readGz("train.json.gz"):
for l in open("user_rating.dat"):

    user,item,rat = l.strip().split()
    if(user in userlist or item in itemlist):
        itemCount[item] += 1
        totalPurchases += 1
        allRatings.append(float(rat))
        userRatings[user].append(float(rat))
        itemRatings[item].append(float(rat))
        if(user not in ur):
            ur.append(user)
        if(item not in ir):
            ir.append(item)
        uiRatings.__setitem__((user,item),float(rat))


    uiRatingsTotal += float(rat)
    iteration = iteration + 1

uiRatingsTotal = (uiRatingsTotal*1.0) / (iteration*1.0)
betauc = {}
betaup = {}

betaic = {}
betaip = {}
msecurrent = 1.0
mseprevious = 11.0
convergeprev = 1.0
convergec  = 0.0


for ui in uiRatings:
    (u,i)= ui
    betaup[u]=0.0
    betaip[i]=0.0
    betauc[u]=0.0
    betaic[i]=0.0
lenui = len(uiRatings)
iter = 1
for ui in uiRatings:
        (u,i)=ui
        msecurrent+= (alphac+betauc[u]+betaic[i]-uiRatings.__getitem__((u,i)))**2
for u in ur:
    convergec+= 2.5*betauc[u]*betauc[u]
for i in ir:
    convergec+=2.5*betaic[i]*betaic[i]
convergec = convergec + msecurrent
mseprevious = msecurrent +2.5
convergeprev = convergec + 2.5

while(convergec<convergeprev):
    mseprevious= msecurrent
    convergeprev=convergec
    iter = iter+ 1
    alphap=alphac
    betaup=betauc.copy()
    betaip=betaic.copy()
    alphac=0.0
    for ui in uiRatings:
        (u,i)= ui
        betaic[i]=0.0
        betauc[u]=0.0

        alphac += ((uiRatings.__getitem__(ui))-(betaup[u]+betaip[i]))/(lenui)

    for ui in uiRatings:
        (u,i)=ui
        betauc[u]+=(uiRatings.__getitem__((u,i))-(alphac+betaip[i]))/(2.5+len(userRatings[u]))

    for ui in uiRatings:
        (u,i)=ui
        betaic[i]+=(uiRatings.__getitem__((u,i))-(alphac+betauc[u]))/(2.5+len(itemRatings[i]))

    msecurrent = 0.0
    convergec = 0.0
    for ui in uiRatings:
        (u,i)=ui
        msecurrent+= (alphac+betauc[u]+betaic[i]-uiRatings.__getitem__((u,i)))**2
    for u in ur:
        convergec+= 2.5*betauc[u]*betauc[u]
    for i in ir:
        convergec+=2.5*betaic[i]*betaic[i]
    convergec+=msecurrent
print msecurrent
print mseprevious