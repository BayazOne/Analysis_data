import networkx as nx
import matplotlib.pyplot as plt

#Центральность для 50 узлов с «ямой» и «горбиком» значений,
#т. е. когда последовательность сначала падает вниз, потом возрастает до пикового значения, а затем снова опускается.

G = nx.tadpole_graph(35, 15)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])

nx.draw(G, with_labels=True)
plt.show()
plt.plot(list(centrality.keys()), list (centrality.values()))
plt.show()
