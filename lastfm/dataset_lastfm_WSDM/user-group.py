import json
from collections import defaultdict
from collections import Counter
dictionary = defaultdict(lambda : defaultdict(list))
user_tags = defaultdict(lambda : defaultdict(int))
for l in open("annotations_filtered.dat", 'r'):
    uid, item_id, tag_id = l.strip().split(',')
    #print uid, item_id, tag_id
    #dictionary['uid']
    dictionary[uid][item_id].append(tag_id)
    user_tags[uid][tag_id]+=1
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
users=[]
for l in open("users.dat", 'r'):
    uid=l.strip()
    users.append(uid)
users=set(users)

group_tags = Counter(defaultdict(list))
UserG = defaultdict(list)
for l in open("groups.dat", 'r'):
    gid, uid = l.strip().split()
    group_tags[gid]+=Counter(user_tags[uid])
    UserG[uid].append(gid)

ms = defaultdict(lambda : defaultdict(list))

for u in users:
    for g in UserG[u]:
        ms[u][g]=0.0
        numerator=0.0
        denominator=0.0
        for Ta in set(user_tags[u]).intersection(set(group_tags[g])):
            numerator+=user_tags[u][Ta]
        for Tu in set(group_tags[g]):
            denominator+=group_tags[Tu]
        ms[u][g]=float(numerator)/float(denominator)

Msim = defaultdict(lambda : defaultdict(list))

for u in users:
    for v in users:
        for g in set(UserG[u]).intersection(UserG[v]):
            Msim[u][v]=ms[u][g]*ms[v][g]
        Msim[u][v]=Msim[u][v]/len(set(UserG[u]).intersection(UserG[v]))


fp=open("Msim.dat", 'w')
for u in users:
    for v in users:
        fp.write(u + ',' + v + ',' + str(Msim[u][v]) + "\n")

'''

Tsim = defaultdict(lambda : defaultdict(list))


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

'''