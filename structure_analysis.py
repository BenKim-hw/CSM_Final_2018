import networkx as nx
import numpy as np
import glob, os
import itertools
import copy
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

for file in glob.glob("gt/data/*.csv"):
    file2 = file.split('\\')
    file3 = file2[1].split('csv')
    
    print(file)
    graph = nx.read_edgelist(file,delimiter='\t')
    X = graph.selfloop_edges()
    graph2 = copy.deepcopy(graph)
    graph2.remove_edges_from(X)
    pr = nx.pagerank_numpy(graph2)
    key = list(pr.keys())
    values = list(pr.values())
    idx = np.argsort(values)[::-1]
    f = open('gt/result/'+'PageRank_'+file3[0]+'txt','w')
    
    print('Node ID\tPageRank score',file = f)
    for index in idx:
        print(key[index]+'\t'+str(values[index])+'\t',file = f)
    
    f2 = open('gt/result/'+'Community_'+file3[0]+'txt','w')
    pos = nx.spring_layout(graph2)
    c = list(greedy_modularity_communities(graph2))
    print('Number of communities:\t'+str(len(c)), file=f2)
    for i in range(len(c)):
        nx.draw_networkx_nodes(graph2, pos, c[i], node_size = 5, node_color = str(i*1.0 / len(c)), label='Community '+str(i))
        print('Community '+str(i)+'\t'+str(sorted(c[i])),file = f2)
    nx.draw_networkx_edges(graph2, pos, alpha=0.2)
    f3 = 'gt/result/'+'Community_'+file3[0]+'png'
    plt.legend()
    plt.savefig(f3,dpi=300)
    plt.show()
