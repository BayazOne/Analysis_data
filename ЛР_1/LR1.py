import math


def arg_min(T, S):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 7, math.inf, math.inf, 4, math.inf),
     (7, 0, 5, math.inf, math.inf, 2),
     (math.inf, 5, 0, 11, math.inf, 6),
     (math.inf, math.inf, 11, 0, 8, 9),
     (4, math.inf, math.inf, 8, 0, 3),
     (math.inf, 2, 6, 9, 3, 0))

N = len(D)  # число вершин в графе
T = [math.inf]*N   # последняя строка таблицы

top_v = int(input("Введите номер начальной вершины: "))  # стартовая вершина (нумерация с нуля)
v = top_v
S = {v}     # просмотренные вершины
T[v] = 0    # нулевой вес для стартовой вершины
M = [0]*N   # оптимальные связи между вершинами

while v != -1:          # цикл, пока не просмотрим все вершины
    for j, dw in enumerate(D[v]):   # перебираем все связанные вершины с вершиной v
        if j not in S:           # если вершина еще не просмотрена
            w = T[v] + dw
            if w < T[j]:
                T[j] = w
                M[j] = v        # связываем вершину j с вершиной v

    v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
    if v >= 0:                    # выбрана очередная вершина
        S.add(v)                 # добавляем новую вершину в рассмотрение


for i in range((N-1), -1, -1):
    C = [i]
    end = i
    while end != top_v:
        end = M[C[-1]]
        C.append(end)
    print("Расстояние от вершины", top_v, "до", i, " = ", str(T[i]).ljust(5), "Путь:", *list(reversed(C)))

