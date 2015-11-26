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


print type(network)
top_artists = collections.defaultdict(lambda : collections.defaultdict(list))
def create_user_data(userlist, layer ):

    if layer == 0 :
        return
    layer = layer - 1
    swaplist = []
    for i in userlist:
        try:
            swaplist = swaplist + i.get_friends()
        except IndexError:
            continue
        newuser =  pylast.Library(i,network)
        templ = newuser.get_artists(50,True)
        if len(top_artists[str(newuser.get_user())][str(newuser.get_user())]) == 0:
            for j in range(len(templ)):
                top_artists[str(newuser.get_user())][str(newuser.get_user())].append([str(templ[j].item),templ[j].playcount])
        create_user_data(swaplist,layer)




create_user_data(user_list,4)
print top_artists['joi']
with open('user.json', 'w') as fp:
    for a in top_artists:
    	json.dump(top_artists[a], fp)
    	fp.write("\n")
print len(top_artists)

