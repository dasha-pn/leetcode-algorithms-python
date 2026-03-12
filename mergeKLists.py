"""Exercise from LeetCode"""

import heapq
from typing import Optional, Iterable

class ListNode:
    """
    Клас вузла однозв'язного списку.

    >>> n3 = ListNode(3)
    >>> n2 = ListNode(2, n3)
    >>> n1 = ListNode(1, n2)
    >>> str(n1)
    '1->2->3'
    """

    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        values = []
        cur = self
        while cur is not None:
            values.append(str(cur.val))
            cur = cur.next
        return "->".join(values)

def build_list(values: Iterable[int]) -> Optional[ListNode]:
    """
    Створює зв'язний список із звичайного Python-ітерабельного (list, tuple...)

    >>> build_list([]) is None
    True
    >>> head = build_list([10, 20, 30])
    >>> str(head)
    '10->20->30'
    """
    it = iter(values)
    try:
        first = next(it)
    except StopIteration:
        return None

    head = ListNode(first)
    tail = head
    for v in it:
        tail.next = ListNode(v)
        tail = tail.next
    return head


def list_to_pylist(head: Optional[ListNode]) -> list[int]:
    """
    Перетворює зв'язний список назад у звичайний Python-список.
    Зручно для перевірки результатів у доктестах.

    >>> list_to_pylist(build_list([1, 2, 3]))
    [1, 2, 3]
    >>> list_to_pylist(None)
    []
    """

    res = []
    cur = head
    while cur is not None:
        res.append(cur.val)
        cur = cur.next
    return res


def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Зливає k відсортованих зв'язних списків в один відсортований список
    і повертає його голову.

    Ідея:
    - тримаємо мін-heap;
    - у heap кладемо (значення, індекс_списку, вузол);
    - кожного разу дістаємо мінімальний вузол і пришиваємо в результат;
    - якщо в цього вузла був next, кладемо його в heap.

    Складність:
    - Нехай N = сума довжин усіх списків.
    - k = кількість списків.
    - Кожен вузол заходить і виходить з heap один раз.
    - Операції з heap коштують O(log k).
    => Часова складність: O(N * log k)
    => Додаткова пам'ять: O(k) для heap.

    Доктести з умови задачі:

    Приклад 1:
    lists = [[1,4,5],[1,3,4],[2,6]]
    Очікуємо: [1,1,2,3,4,4,5,6]

    >>> l1 = build_list([1,4,5])
    >>> l2 = build_list([1,3,4])
    >>> l3 = build_list([2,6])
    >>> ans = mergeKLists([l1, l2, l3])
    >>> list_to_pylist(ans)
    [1, 1, 2, 3, 4, 4, 5, 6]

    Приклад 2:
    lists = []
    Очікуємо: []

    >>> ans2 = mergeKLists([])
    >>> list_to_pylist(ans2)
    []

    Приклад 3:
    lists = [[]]
    Очікуємо: []

    >>> ans3 = mergeKLists([build_list([])])
    >>> list_to_pylist(ans3)
    []

    Ще один тест: одна з порожніх, одна непорожня

    >>> a = build_list([])
    >>> b = build_list([0, 10, 10])
    >>> list_to_pylist(mergeKLists([a, b]))
    [0, 10, 10]

    Спадні значення не повинні бути, але негативні дозволені:
    >>> c1 = build_list([-5, -1, 2])
    >>> c2 = build_list([-3, 4])
    >>> list_to_pylist(mergeKLists([c1, c2]))
    [-5, -3, -1, 2, 4]
    """
    # мін-heap (пріоритетна черга)
    heap: list[tuple[int, int, ListNode]] = []

    # 1. покласти перші елементи всіх непорожніх списків у heap
    for i, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, i, node))

    # фіктивна голова, щоб зручно будувати результат
    dummy = ListNode()
    tail = dummy

    # 2. доти, доки heap не спорожніє
    while heap:
        # забрати найменший елемент
        val, i, node = heapq.heappop(heap)

        # пришити цей вузол у кінець відповіді
        tail.next = node
        tail = tail.next

        # якщо в нього є наступний елемент — покласти його в heap
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, i, node.next))

    # справжня голова — після dummy
    return dummy.next

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
