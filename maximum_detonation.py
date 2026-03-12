"""Exercise from LeetCode"""

from collections import deque

def maximum_detonation(bombs):
    """..."""

    n = len(bombs)

    # 1. Побудова орієнтованого графа досяжності
    graph = [[] for _ in range(n)]
    for i in range(n):
        x1, y1, r1 = bombs[i]
        r1_sq = r1 * r1  # радіус у квадраті
        for j in range(n):
            if i == j:
                continue
            x2, y2, _ = bombs[j]
            dx = x1 - x2
            dy = y1 - y2
            dist_sq = dx * dx + dy * dy  # квадрат відстані між центрами
            if dist_sq <= r1_sq:
                # i може підірвати j
                graph[i].append(j)

    # 2. Функція BFS/DFS для підрахунку, скільки бомб злетить,
    #    якщо почати з бомби start
    def bfs_count(start):
        visited = set([start])
        q = deque([start])

        while q:
            cur = q.popleft()
            for nei in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return len(visited)

    # 3. Пробуємо кожну бомбу як стартову і беремо максимум
    ans = 0
    for i in range(n):
        ans = max(ans, bfs_count(i))

    return ans

print(maximum_detonation([[2,1,3],[6,1,4]]))                  # очікуємо 2
print(maximum_detonation([[1,1,5],[10,10,5]]))                # очікуємо 1
print(maximum_detonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))  # очікуємо 5
