import operator
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def test(graph_directory,txt_directory):
    graph = nx.read_graphml(graph_directory)
    print nx.info(graph)
    output = open(txt_directory,'w')
    dd = {}
    for i in graph.edges():
        weight = graph.get_edge_data(i[0],i[1])
        print weight
        break

def g_weight(graph_directory,txt_directory):
    graph = nx.read_graphml(graph_directory)
    degrees = [x[1] for x in graph.degree()]
    print sorted(degrees)
    plt.loglog(sorted(degrees,reverse=True),'o')
    plt.xlabel('rank')
    plt.ylabel('degree')
    plt.show()
    output = open(txt_directory,'w')
    dd = {}
    nl = []
    for i in graph.nodes():
        nl.append(int(i.split('n')[1]))
    key = min(nl)
    if key != 0 and key != 1:
        print "error, min = " , key
    for i in graph.edges():
        weight = graph.get_edge_data(i[0],i[1])
        try:
            w = weight['weight']
        except:
            w = -1
        idx1 = int(i[0].split('n')[1])+(1-key)
        idx2 = int(i[1].split('n')[1])+(1-key)
        dd[(idx1,idx2)] = w
    dk = dd.keys()
    dk.sort(key=operator.itemgetter(0,1))
    for i in dk:
        output.write(str(i[0])+'\t'+str(i[1])+'\t'+str(dd[i])+'\n')
    output.close()


def g_weight1(graph_directory,txt_directory):
    graph = nx.read_graphml(graph_directory)
    degrees = [x[1] for x in graph.degree()]
    output = open(txt_directory,'w')
    plt.loglog(sorted(degrees,reverse=True),'o')
    plt.xlabel('rank')
    plt.ylabel('degree')
    plt.show()
    dd = {}
    nl = []
    for i in graph.nodes():
        nl.append(int(i.split('n')[1]))
    key = min(nl)
    if key != 0 and key != 1:
        print "error, min = " , key
    for i in graph.edges():
        weight = graph.get_edge_data(i[0],i[1])
        try:
            w = weight[0]['weight']
        except:
            w = -1
        idx1 = int(i[0].split('n')[1])+(1-key)
        idx2 = int(i[1].split('n')[1])+(1-key)
        dd[(idx1,idx2)] = w

    dk = dd.keys()
    dk.sort(key=operator.itemgetter(0,1))
    for i in dk:
        output.write(str(i[0])+'\t'+str(i[1])+'\t'+str(dd[i])+'\n')
    output.close()

def g_weight2(graph_directory,txt_directory):
    graph = nx.read_graphml(graph_directory)
    degrees = [x[1] for x in graph.degree()]
    output = open(txt_directory,'w')
    plt.loglog(sorted(degrees,reverse=True),'o')
    plt.xlabel('rank')
    plt.ylabel('degree')
    plt.show()
    dd = {}
    nl = []
    for i in graph.nodes():
        nl.append(int(i.split('n')[1]))
    key = min(nl)
    if key != 0 and key != 1:
        print "error, min = " , key
    for i in graph.edges():
        weight = graph.get_edge_data(i[0],i[1])
        try:
            wc = weight['w_contra_weight']
        except:
            wc = -1
        try:
            wi = weight['w_ipsi_weight']
        except:
            wi = -1
        idx1 = int(i[0].split('n')[1])+(1-key)
        idx2 = int(i[1].split('n')[1])+(1-key)
        dd[(idx1,idx2)] = max(wc,wi)

    dk = dd.keys()
    dk.sort(key=operator.itemgetter(0,1))
    for i in dk:
        output.write(str(i[0])+'\t'+str(i[1])+'\t'+str(dd[i])+'\n')
    output.close()

def g_weight3(graph_directory,txt_directory):
    graph = nx.read_graphml(graph_directory)
    degrees = [x[1] for x in graph.degree()]
    plt.loglog(sorted(degrees,reverse=True),'o')
    plt.xlabel('rank')
    plt.ylabel('degree')
    plt.show()
    output = open(txt_directory,'w')
    dd = {}
    nl = []
    for i in graph.nodes():
        nl.append(int(i.split('n')[1]))
    key = min(nl)
    nl.sort()
    if key != 0 and key != 1:
        print "error, min = " , key
    for i in graph.edges():
        weight = graph.get_edge_data(i[0],i[1])
        try:
            ew = weight['electrical_weight']
        except:
            ew = -1
        try:
            cw = weight['chemical_weight']
        except:
            cw = -1
        idx1 = int(i[0].split('n')[1])+(1-key)
        idx2 = int(i[1].split('n')[1])+(1-key)
        dd[(idx1,idx2)] = max(ew,cw)

    dk = dd.keys()
    dk.sort(key=operator.itemgetter(0,1))
    for i in dk:
        output.write(str(i[0])+'\t'+str(i[1])+'\t'+str(dd[i])+'\n')
    output.close()

def main():
    g_weight3('c.elegans_neural.male_1.graphml','c.elegans_neural.male_1.txt')
    g_weight1('c.elegans.herm_pharynx_1.graphml','c.elegans.herm_pharynx_1.txt')
    g_weight('rattus.norvegicus_brain_1.graphml','rattus.norvegicus_brain_1.txt')
    g_weight2('mouse_brain_1.graphml','mouse_brain_1.txt')
    g_weight1('mouse_retina_1.graphml','mouse_retina_1.txt')
    g_weight('mouse_visual.cortex_2.graphml','mouse_visual.cortex_2.txt')
    g_weight('rhesus_brain_1.graphml','rhesus_brain_1.txt')
    g_weight('rhesus_interareal.cortical.network_2.graphml','rhesus_interareal.cortical.network_2.txt')
    g_weight('cat.graphml','cat.txt')
    g_weight('drosophila_medulla_1.graphml','drosophila_medulla_1.txt')

if __name__ == '__main__':
    main()
