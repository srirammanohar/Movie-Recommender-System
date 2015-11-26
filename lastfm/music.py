__author__ = 'sriram'
import pylast
import single_init
network = pylast.LastFMNetwork(api_key = single_init.API_KEY, api_secret =
    single_init.API_SECRET, username = single_init.username, password_hash = single_init.password_hash)
user =  network.get_user('RJ')
a = user.get_friends()
a = [str(a[i]) for i in range(len(a))]
print a
print a[1]
print len(a)
print user