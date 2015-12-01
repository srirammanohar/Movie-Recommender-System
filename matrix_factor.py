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

for i in rank:
    rank[i] = sorted(rank[i],key = lambda x: x[1])


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

user_list = set()
user_grp_length=defaultdict(list)
for l in open("user_rating.dat"):
    uid,iid,rank = l.strip().split()
    if uid not in user_list:
        user_list.add(uid)
        user_grp_length[uid]=[0,0,0,0]
    elif rank>3:
        user_grp_length[uid][3]+=1
    elif rank>2:
        user_grp_length[uid][2]+=1
    elif rank>1:
        user_grp_length[uid][1]+=1
    else:
        user_grp_length[uid][0]+=1


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
        if r>3:
            er[i] = (r - g[0][0])/((user_grp_length[i])[3])**.5
        elif r>2:
            er[i] = (r - g[0][0])/((user_grp_length[i])[2])**.5
        elif r>1:
            er[i] = (r - g[0][0])/((user_grp_length[i])[1])**.5
        else:
            er[i] = (r - g[0][0])/((user_grp_length[i])[0])**.5

        for j in range(dim):
            u[us][j] = u[us][j]+ gamma*((er[i]*p[pr][j])- lam*u[us][j] )
            p[pr][j] = p[pr][j] + gamma*((er[i]*u[us][j]) - lam*p[pr][j])

        curr_err += er[i]*er[i] + lam*((a*at)[0][0] + (b*bt)[0][0])
print "prev_error"
print prev_error
print "curr_error"
print curr_err



