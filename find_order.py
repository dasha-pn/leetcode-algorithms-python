"""Exercise 3 from LeetCode"""

from collections import defaultdict

def find_order(num_courses, prerequisites):
    """
    >>> find_order(4, [[1,0],[2,0],[3,1],[3,2]])
    [0, 2, 1, 3]
    >>> find_order(2, [[1,0]])
    [0, 1]
    >>> find_order(1, [])
    [0]
    >>> find_order(3, [[1,0],[1,2],[0,1]])
    []
    """

    #adj: список суміжності орієнтованого графа
    #Граф: b -> a (щоб взяти a, треба спершу b)
    adj = defaultdict(list)
    indeg = [0]*num_courses

    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    # Використаємо стек (LIFO), щоб при обробці 0 спершу вийшов 2, потім 1
    #Усі курси без передумов (вхідний степінь 0) кидаємо у stack.
    #Це стартові вершини для топологічного сорту (алгоритм Кана).
    stack = []
    for i in range(num_courses):
        if indeg[i] == 0:
            stack.append(i)

    res = []

    #Поки є вершини без вхідних ребер
    while stack:
        u = stack.pop()
        res.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)

    return res if len(res) == num_courses else []

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
