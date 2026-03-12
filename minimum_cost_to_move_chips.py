"""Exercise from LeetCode"""

def min_cost_to_move_chips(position: list[int]) -> int:
    """
    Повертає мінімальну вартість зведення всіх фішок в одну позицію.

    Логіка: рух на ±2 безкоштовний, тому всередині однієї парності (парні/непарні)
    можна все зібрати за 0. Платимо лише за переведення між парностями.
    Отже, відповідь = min(#парних, #непарних).

    >>> min_cost_to_move_chips([1, 2, 3])
    1
    >>> min_cost_to_move_chips([2, 2, 2, 3, 3])
    2
    >>> min_cost_to_move_chips([1, 1000000000])
    1
    >>> min_cost_to_move_chips([2, 4, 6])  # усі парні, все безкоштовно
    0
    >>> min_cost_to_move_chips([1, 3, 5, 7])  # усі непарні, теж 0
    0
    """

    even = 0
    odd = 0

    for el in position:
        if el % 2 == 0:
            even += 1
        else:
            odd += 1

    return min(even, odd)

if __name__ == "__main__":
    print(min_cost_to_move_chips([1, 2, 3]))           # 1
    print(min_cost_to_move_chips([2, 2, 2, 3, 3]))     # 2
    print(min_cost_to_move_chips([1, 1000000000]))     # 1
    import doctest
    doctest.testmod(verbose=True)
