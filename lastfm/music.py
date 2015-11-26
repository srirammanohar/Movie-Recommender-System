__author__ = 'sriram'
import pylast
import single_init
import collections
network = pylast.LastFMNetwork(api_key = single_init.API_KEY, api_secret =
    single_init.API_SECRET, username = single_init.username, password_hash = single_init.password_hash)
user =  pylast.Library('RJ',network)
friends =[]
print type(user)
print user

#friends = user.getFriends()
#a = user.get_recent_tracks()
print type(network)
#a = [str(a[i]) for i in range(len(a))]
top_artists=collections.defaultdict(list)
temp=user.get_artists(50,True)
for i in range(len(temp)):
    top_artists[user].append([str(temp[i].item), temp[i].playcount])

print top_artists
#user.get_artists(50,True)[0].playcount

friends = user.get_user().get_friends()
for i in friends:

    friends2 = i.get_friends()
    for k in friends2:
        newuser =  pylast.Library(k,network)
        templ = newuser.get_artists(50,True)
        for j in range(len(templ)):
            top_artists[newuser].append([str(templ[j].item),templ[j].playcount])



print len(top_artists)
print len(friends)
for i in range(10):
    print top_artists[i]


