import networkx as nx
import matplotlib.pyplot as plt

#Центральность для семи узлов с пиком на конце
G = nx.path_graph(5)
G.add_nodes_from([6, 7])
G.add_edges_from([(4, 7), (5, 7), (6, 7)])
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])

nx.draw(G, with_labels=True)
plt.show()
