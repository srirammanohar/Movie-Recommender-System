import json
import time
from collections import defaultdict
dictionary = defaultdict(lambda : defaultdict(list))
users=[]
items=[]
item_tags=defaultdict(lambda: defaultdict(int))
for l in open("user_taggedartists.dat", 'r'):
    if l.startswith("userID"):
       continue
    uid, item_id, tag_id, day, month, year = l.strip().split()
    #print uid, item_id, tag_id
    #dictionary['uid']
    users.append(uid)
    items.append(item_id)
    dictionary[uid][item_id].append(tag_id)
    item_tags[item_id][tag_id]+=1    
    #break

Tsim = defaultdict(lambda : defaultdict(float))
users=set(users)
items=set(items)
print users
print "reading done"

for u in users:
    #print time.time()
    ItemU=set(dictionary[u].keys())
    for v in users:
        Tsim[u][v]=0.0
        ItemV=set(dictionary[v].keys())
        Intersect=ItemU.intersection(ItemV)
        for i in Intersect:
            Tsim[u][v]+=float(len(set(dictionary[u][i]).intersection(dictionary[v][i]))**2)/float(len(dictionary[u][i])*len(dictionary[v][i]))
        if max(len(ItemU), len(ItemV)) > 0.0:
            Tsim[u][v]=Tsim[u][v]/max(len(ItemU), len(ItemV))

print "writing Tsim"
fp=open("Tsim.dat", 'w')
for u in users:
    for v in users:
        fp.write(u + ',' + v + ',' + str(Tsim[u][v]) + "\n")

fp.close()
print "done Tsim"

Fsim = defaultdict(lambda : defaultdict(float))
friends=set()
for l in open("user_friends.dat", 'r'):
    u, v = l.strip().split()
    friends.add((u,v))

SumF=0.0
AvgF=0.0
for u in users:
    count=0.0
    AvgF=0.0
    for k in Tsim[u]:
        if (u, k) not in friends:
            continue
        SumF+=Tsim[u][k]
        count+=1.0
    if count > 0.0:
        AvgF=SumF/count
    for v in users:
        if (u,v) not in friends or Tsim[u][v]<AvgF:
            Fsim[u][v]=0
            continue
        Fsim[u][v]=Tsim[u][v]/(1.0+Tsim[u][v]-AvgF)

print "writing Fsim"
fp=open("Fsim.dat", 'w')
for u in users:
    for v in users:
        if (u,v) not in friends:
            continue
        fp.write(u + ',' + v + ',' + str(Fsim[u][v]) + "\n")
fp.close()

print "done Fsim"

alpha=0.7
Sim = defaultdict(lambda : defaultdict(float))

for u in users:
    for v in users:
        Sim[u][v]=(alpha*Tsim[u][v])+(1.0-alpha)*Fsim[u][v]

SimItem = defaultdict(lambda : defaultdict(float))
print len(items)
for i in items:
    print time.time()
    for j in items:
        SimItem[i][j]=0.0
        denominator=0.0
        for t in set(item_tags[i]).intersection(set(item_tags[j])):
            SimItem[i][j]+=min(item_tags[i][t], item_tags[j][t])
            denominator+=max(item_tags[i][t], item_tags[j][t])
        for ta in  (set(item_tags[i]).union(set(item_tags[j]))).difference(set(item_tags[i]).intersection(set(item_tags[j]))):
            denominator+=max(item_tags[i][ta], item_tags[j][ta])
        SimItem[i][j]=float(SimItem[i][j])/float(denominator)

print "write ItemSim"
fp=open("ItemSim.dat", 'w')
for i in items:
    for j in items:
        fp.write(i + ',' + j + ',' + str(SimItem[i][j]) + "\n")
fp.close()
