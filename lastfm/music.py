__author__ = 'sriram'
import pylast
import single_init
import collections
import json

network = pylast.LastFMNetwork(api_key = single_init.API_KEY, api_secret =
    single_init.API_SECRET, username = single_init.username, password_hash = single_init.password_hash)
user =  pylast.Library('joi',network)
friends =[]
print type(user)
print user
user_list = []
user_list.append(user.get_user())

#frie= nds = user.getFriends()
#a = user.get_recent_tracks()
print type(network)
#a = [str(a[i]) for i in range(len(a))]
top_artists = collections.defaultdict(lambda : collections.defaultdict(list))
# temp=user.get_artists(50,True)
# for i in range(len(temp)):
# #user.get_artists(50,True)[0].playcount
#     top_artists[user.get_user()].append([str(temp[i].item), temp[i].playcount])
#
# print top_artists
#
# friends = user.get_user().get_friends()
# for i in friends:
#
#     friends2 = i.get_friends()
#     len = len(friends2)
#     for k in friends2:
#         newuser =  pylast.Library(k,network)
#         templ = newuser.get_artists(50,True)
#         if len(top_artists[newuser.get_user()]) == 0:
#             for j in range(len(templ)):
#                 top_artists[newuser.get_user()].append([str(templ[j].item),templ[j].playcount])
#


def create_user_data(userlist, layer ):
    try:
        if layer == 0 :
            return
        layer = layer - 1
        swaplist = []
        for i in userlist:
            swaplist = swaplist + i.get_friends()
            newuser =  pylast.Library(i,network)
            templ = newuser.get_artists(50,True)
            if len(top_artists[str(newuser.get_user())][str(newuser.get_user())]) == 0:
                for j in range(len(templ)):
                    top_artists[str(newuser.get_user())][str(newuser.get_user())].append([str(templ[j].item),templ[j].playcount])
        create_user_data(swaplist,layer)
    except IndexError:
        print i

create_user_data(user_list,2)
print top_artists['joi']
with open('user.json', 'w') as fp:
    for a in top_artists:
    	json.dump(top_artists[a], fp)
    	fp.write("\n")
print len(top_artists)

# count = 0
# for i in top_artists:
#     print top_artists[i]
#     print type(top_artists[i])
#     count += 1
#     if count>10:
#         break
#
