import networkx as nx
import matplotlib.pyplot as plt
# кол-во вершин
n = 10
# вероятность появления случайного ребра
p = 0.3

# генерация графа
G = nx.erdos_renyi_graph(n, p)

# рассчёт средней степени вершин графа. (Кол.-во ребер инцидентных вершинам.)
a = 0
for i in G.nodes():
    a = a + G.degree(i)

# средняя степень вершины фактическая
a_avr = float(a) / len(G.nodes())

# средняя степень вершины по формуле
calc_avr = (n-1)*p

# разница значений
div_a = calc_avr - a_avr
print("Средняя степень вершины фактическая: ", round(a_avr, 3))
print("Средняя степень вершины по формуле: ", round(calc_avr, 3))
print("Полученная разница значений: ", round(div_a, 3))

nx.draw(G, with_labels=True)
plt.show()
