__author__ = 'sriram'
import json
from collections import defaultdict
from operator import itemgetter
import time
global_user =  defaultdict(int)
user_artist = defaultdict(int)
user = []
artist = []
rank = defaultdict(list)
for l in open("user_artists.dat",'r'):
    [uid , aid , freq] = l.strip().split()
    if uid == 'userID':
        continue;

    f = int(freq)
    if uid not in user:
        user.append(uid)
    if aid not  in artist:
        artist.append(aid)
    user_artist[(uid,aid)]=f
    if uid in global_user:
        global_user[uid]+=f
    else:
        global_user[uid]=f

for l in open("user_artists.dat",'r'):
    [uid , aid , freq] = l.strip().split()
    if uid == 'userID':
        continue;
    f = int(freq)
    rank[uid].append((aid,f))

print rank['2']
for i in rank:
    rank[i] = sorted(rank[i],key = lambda x: x[1])
    if i == '2':
        print rank[i]
print rank['2']

with open("user_artists.dat") as f:
    f.seek(0)
    f.next()
    with open("user_rating.dat", "w") as f1:
        for line in f:
            [uid , aid , freq] = line.strip().split()
            for i in rank[uid]:
                if i[0] == aid:
                    k=rank[uid].index(i)
                    if (uid == '2'):
                        print k

            gf = 0
            for i in range(0,k):
                (a,f)=rank[uid][i]
                gf+= float(f)/float(global_user[uid])

            freq_imp = 4* (1-gf)
            f1.write(uid + " " + aid + " "+ str(freq_imp) + "\n")


# print global_user['2']