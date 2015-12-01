from collections import defaultdict

no_of_users = defaultdict(int)
no_of_items = defaultdict(int)
no_of_tags = defaultdict(int)




for l in open("user_taggedartists.dat", 'r'):
    if l.startswith("userID"):
       continue
    uid, item_id, tag_id, day, month, year = l.strip().split()
    #print uid, item_id, tag_id
    #dictionary['uid']
    no_of_users[uid]+=1
    no_of_items[item_id]+=1
    no_of_tags[tag_id]+=1

    #break
print len(no_of_users)
print len(no_of_items)
print len(no_of_tags)

friends = defaultdict(int)
for l in open("user_friends.dat", 'r'):
	uid, friendid = l.strip().split()
	friends[uid]+=1

users=set()
items=set()
tags=set()

j=0
for i in friends:
	if friends[i]>1:
		j+=1
print j

fp=open("user_friends_new.dat", 'w')
for l in open("user_friends.dat", 'r'):
    if l.startswith("userID"):
       continue
    uid, fid = l.strip().split()
    #print uid, item_id, tag_id
    #dictionary['uid']
    #if no_of_tags[tag_id]>5 and no_of_items[item_id]>10:
    #if no_of_tags[uid]>5:
    if friends[uid]>1 and friends[fid]>1:
        fp.write(str(uid)+' '+str(fid)+"\n")

fp.close()


fp=open("user_artists_new.dat", 'w')
for l in open("user_artists.dat", 'r'):
    if l.startswith("userID"):
       continue
    uid, aid, weight = l.strip().split()
    #print uid, item_id, tag_id
    #dictionary['uid']
    #if no_of_tags[tag_id]>5 and no_of_items[item_id]>10:
    #if no_of_tags[uid]>5:
    if friends[uid]>1:
        fp.write(str(uid)+' '+str(aid)+' '+str(weight)+"\n")

fp.close()


fp=open("user_taggedartists_new.dat", 'w')
for l in open("user_taggedartists.dat", 'r'):
    if l.startswith("userID"):
       continue
    uid, item_id, tag_id, day, month, year = l.strip().split()
    #print uid, item_id, tag_id
    #dictionary['uid']
    #if no_of_tags[tag_id]>5 and no_of_items[item_id]>10:
    #if no_of_tags[uid]>5:
    if friends[uid]>1: #and no_of_tags[uid]>5:
        fp.write(str(uid)+' '+str(item_id)+' '+str(tag_id)+' '+str(day)+' '+str(month)+' '+str(year)+"\n")
        users.add(uid)
        items.add(item_id)
        tags.add(tag_id)

fp.close()

print len(users)
print len(items)
print len(tags)

