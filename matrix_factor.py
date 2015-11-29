__author__ = 'sriram'
import json
from collections import defaultdict
from operator import itemgetter
import time
import  numpy
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
dim = 20
lam = 0.8
gamma = 0.0002
u = defaultdict(list)
p = defaultdict(list)
user_rating = defaultdict(int)
er = defaultdict(int)
with open("user_rating.dat", "r") as f1:
    f1.seek(0)
    for line in f1:
        [uid,aid,r1] = line.strip().split()
        r = float(r1)
        u[uid] = [0.1*k for k in range(dim)]
        p[aid] = [0.09*k for k in range(dim)]
        user_rating[(uid,aid)]= r

prev_error = 25504871.0
curr_err = 25504870.0
while (curr_err<prev_error):
    prev_error = curr_err
    curr_err = 0

    for i in user_rating:
        r = user_rating[i]
        (us,pr) = i
        a = u[us]
        a = numpy.array(a)
        a= numpy.matrix(a)

        at = a.transpose()
        #print at
        b = numpy.array(p[pr])
        b = numpy.matrix(b)
        bt = numpy.transpose(b)
        #print type(at)
       # print type(b)
        #print at
        #print b
        #print "m"
        g = a*bt

        er[i] = (r - g[0][0])
        for j in range(dim):
            u[us][j] = u[us][j]+ gamma*((er[i]*p[pr][j])- lam*u[us][j] )
            p[pr][j] = p[pr][j] + gamma*((er[i]*u[us][j]) - lam*p[pr][j])

        curr_err += er[i]*er[i] + lam*((a*at)[0][0] + (b*bt)[0][0])
print "prev_error"
print prev_error
print "curr_error"
print curr_err



