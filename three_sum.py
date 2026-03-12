"""3_sum """

def three_sum(nums: list):
    """
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, 0, 1], [-1, -1, 2]]
    """

    res = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = sorted([nums[i], nums[j], nums[k]])
                    if trip not in res:
                        res.append(trip)

    return res

# сортуємо масив, для кожного i шукаємо пару left,right так,
# щоб сума була нуль — це дає O(n^2) і автоматично зручніше уникати дублікатів.

def three_sum1(nums: list[int]) -> list[list[int]]:
    """
    >>> three_sum1([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    """

    nums.sort()
    res = []
    n = len(nums)

    for i in range(n-2):
        # пропускаємо дублікати на позиції i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                # пересуваємо та пропускаємо дублікати
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
