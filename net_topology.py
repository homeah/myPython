#!/usr/bin/env python
#coding:utf-8
import networkx as nx
def get_path_weight(G,path):
    _weight = 0
    for edge in nx.utils.pairwise(path):
        _weight += G.edges[edge[0],edge[1]]["weight"]
    return _weight

nodes = ["BJ","SH","GZ","HZ","NJ","WH","XA"] #7个节点
G = nx.Graph() #初始化图像
for node in nodes:
    G.add_node(node) #逐个节点加入到图像

#edges就是节点之间的连线
edges = [('BJ', 'SH', 1200), ('BJ', 'GZ', 2500), ('SH', 'GZ', 1300), ('HZ', 'SH', 280), ('HZ', 'GZ', 1000), ('NJ', 'SH', 300), ('NJ', 'BJ', 900), ('WH', 'SH', 800), ('WH', 'BJ', 850), ('XA', 'GZ', 2600), ('XA', 'BJ', 2000)]

G.add_weighted_edges_from(edges) #连线加入图像

for path in nx.shortest_simple_paths(G,"XA","HZ",weight = "weight"): #从cost最小路径开始，给出"XA"-"HZ"可用路径
    print(path,get_path_weight(G,path)) 


