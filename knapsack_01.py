from typing import List, Tuple

def knapsack_01(weights: List[int], values: List[int], W: int) -> Tuple[int, List[int]]:
    """
    0/1 Knapsack (DP з відновленням набору).
    Повертає (максимальна_цінність, список_індексів_вибраних_предметів).

    >>> knapsack_01([2,3,4], [3,4,5], 5)
    (7, [0, 1])
    >>> knapsack_01([2,3,4,5], [3,4,5,8], 5)
    (8, [3])
    >>> knapsack_01([1,2,3], [6,10,12], 5)
    (22, [1, 2])
    """

    n = len(weights)
    assert n == len(values), "weights і values мають бути однакової довжини"
    # dp[i][w] — макс. цінність з перших i предметів при місткості w
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        wi, vi = weights[i-1], values[i-1]
        for w in range(0, W+1):
            # пробуємо взяти i-й
            if wi <= w:
                dp[i][w] = max(dp[i][w], vi + dp[i-1][w-wi])
            # не беремо i-й
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлення набору
    res_value = dp[n][W]
    chosen: List[int] = []
    i, w = n, W
    while i > 0:
        if dp[i][w] != dp[i-1][w]:           # предмет i-1 узяли
            chosen.append(i-1)
            w -= weights[i-1]
        i -= 1
    chosen.reverse()
    return res_value, chosen


def knapsack_01_value_only(weights: List[int], values: List[int], W: int) -> int:
    """
    0/1 Knapsack (1D DP, лише максимальна цінність, без відновлення).
    >>> knapsack_01_value_only([2,3,4], [3,4,5], 5)
    7
    """

    n = len(weights)
    dp = [0]*(W+1)

    for i in range(n):
        wi, vi = weights[i], values[i]
        # з права наліво — щоб кожен предмет використовувався 0/1 раз
        for w in range(W, wi-1, -1):
            cand = vi + dp[w - wi]
            if cand > dp[w]:
                dp[w] = cand
    return dp[W]


if __name__ == "__main__":
    # Приклади
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 8]
    cap = 5
    best, items = knapsack_01(w, v, cap)
    print("Max value:", best)
    print("Chosen items (indices):", items)
    print("Value only (1D):", knapsack_01_value_only(w, v, cap))
