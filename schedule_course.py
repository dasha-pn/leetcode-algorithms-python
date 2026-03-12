"""Exercise from LeetCode"""

import heapq

def schedule_course(courses: list[list[int]]) -> int:
    """
    >>> schedule_course([[100,200],[200,1300],[1000,1250],[2000,3200]])
    3
    >>> schedule_course([[1,2]])
    1
    >>> schedule_course([[3,2],[4,3]])
    0
    """

    courses.sort(key = lambda x: x[1])
    total = 0
    max_heap = []

    for duration, last_day in courses:
        total += duration
        heapq.heappush(max_heap, -duration)

        if total > last_day:
            longest = -heapq.heappop(max_heap)
            total -= longest

    return len(max_heap)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
