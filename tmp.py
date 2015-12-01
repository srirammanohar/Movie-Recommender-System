import networkx as nx
from collections import defaultdict
from operator import itemgetter
import numpy

edges = set()
nodes = set()
i=0
G=nx.Graph()

for line in open('/Users/Rudra/PycharmProjects/assi2/lastfm/user_friends_new.dat', 'r'):
    item = line.rstrip()
    if i==0:
      i+=1
      continue
    else:
      x,y = item.split()
      edges.add((x,y))
      edges.add((y,x))
      nodes.add(x)
      nodes.add(y)

for n in nodes :
  G.add_node(n)

for e in edges :
  G.add_edge(*e)



preference_user=defaultdict(list)
items=set()
weight_user=defaultdict(lambda: defaultdict(int))
for line in open('/Users/Rudra/PycharmProjects/assi2/lastfm/user_artists_new.dat', 'r'):
    uid, item_id, weight = line.strip().split()
    preference_user[uid].append([item_id, int(weight)])
    items.add(item_id)
    weight_user[uid][item_id]+=int(weight)

for a in preference_user:
  x=[elem[1] for elem in preference_user[a]]
  preference_user[a]=[(elem[0], 1.0*elem[1]/numpy.mean(x)) for elem in preference_user[a]]
  #print preference_user[a]

for a in preference_user:
  preference_user[a]=sorted(preference_user[a],key=itemgetter(1), reverse=True)

for cliq_sz in range(2,3):
  cliques=[[]*1000]*1000
  top_N=3
  j=0
  #cliques=nx.k_clique_communities(G,3)
  for i in nx.k_clique_communities(G,cliq_sz):
    cliques[j]= list(i)
    print cliques[j]
    j+=1
  cliques=sorted(cliques,key=len, reverse=True)

  #print cliques[0]
  overall_sum=0.0
  overall_len=0.0
  for k in range(0,j):
    overall_wt=defaultdict(int)

    for elem in cliques[k]:
      x=[elo[1] for elo in preference_user[elem]]
      maxi=max(x)
      for item_id in weight_user[elem].keys():
        overall_wt[item_id]+=1.0*weight_user[elem][item_id]

    overall_wt=sorted(overall_wt.items(), key=itemgetter(1), reverse=True)

    overall_wt=overall_wt[0:top_N]
    #overall_wt=[('289', 43.27262462775934), ('89', 30.240944149222756), ('72', 27.453507518961676)]#, ('227', 19.92286514058814), ('67', 18.346709186929193)]

    #print overall_wt
    '''
    for elem in cliques[0]:
      for i in preference_user[elem][0:top_N]:
        print i[0]
    '''
    count=0
    sum=0.0
    for elem in cliques[k]:
      count=0
      for (a, b) in overall_wt:
        for i in preference_user[elem][0:top_N]:
          if int(a)==int(i[0]):
            count+=1
      #print 1.0*count/5
      sum+=1.0*count/top_N
    overall_sum+=len(cliques[k])*sum/len(cliques[k])
    overall_len+=len(cliques[k])
  print 1.0*overall_sum/overall_len
  #print len(cliques[k])
    #cliques[0]
    #1.30434782609
    #1.35093167702

