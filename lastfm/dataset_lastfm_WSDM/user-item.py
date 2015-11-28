import json
from collections import defaultdict
dictionary = defaultdict(lambda : defaultdict(list))
for l in open("annotations_filtered.dat", 'r'):
    uid, item_id, tag_id = l.strip().split(',')
    #print uid, item_id, tag_id
    #dictionary['uid']
    dictionary[uid][item_id].append(tag_id)
    #break
'''
with open('user-item.json', 'w') as fp:
    for a in dictionary:
        json.dump(dictionary[a], fp)
        fp.write("\n")

with open('user-item.json', 'r') as data_file:
    print json.load(data_file)
   
print data[0]
'''
Tsim = defaultdict(lambda : defaultdict(list))

users=[]
for l in open("users.dat", 'r'):
    uid=l.strip()
    users.append(uid)
users=set(users)
for u in users:
    ItemU=set(dictionary[u].keys())
    for v in users:
        Tsim[u][v]=0.0
        ItemV=set(dictionary[v].keys())
        Intersect=ItemU.intersection(ItemV)
        for i in Intersect:
            Tsim[u][v]+=float(len(set(dictionary[u][i]).intersection(dictionary[v][i]))**2)/float(len(dictionary[u][i])*len(dictionary[v][i]))
        if max(len(ItemU), len(ItemV)) > 0.0:
            Tsim[u][v]=Tsim[u][v]/max(len(ItemU), len(ItemV))

fp=open("Tsim.dat", 'w')
for u in users:
    for v in users:
        fp.write(u + ',' + v + ',' + str(Tsim[u][v]) + "\n")

fp.close()

Fsim = defaultdict(lambda : defaultdict(list))
friends=set()
for l in open("friends.dat", 'r'):
    u, v = l.strip().split()
    friends.add((u,v))

SumF=0.0
AvgF=0.0
for u in users:
    for k in Tsim[u]:
        SumF+=Tsim[u][k]
    AvgF=SumF/len(Tsim[u].keys())
    for v in users:
        if (u,v) not in friends or Tsim[u][v]<AvgF:
            Fsim[u][v]=0
            continue
        Fsim[u][v]=Tsim[u][v]/(1+Tsim[u][v]-AvgF)

fp=open("Fsim.dat", 'w')
for u in users:
    for v in users:
        if (u,v) not in friends:
            continue
        fp.write(u + ',' + v + ',' + str(Fsim[u][v]) + "\n")
fp.close()

