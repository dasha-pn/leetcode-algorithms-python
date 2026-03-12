# LeetCode Algorithms in Python

This repository contains Python implementations of various **algorithmic problems** commonly found on platforms such as **LeetCode**.

The solutions demonstrate different algorithmic techniques including:

- dynamic programming
- graph traversal
- greedy algorithms
- prefix sums
- heaps
- two pointers
- combinatorics

---


Each file contains:

- implementation
- explanation
- doctests for verification.

---

# Implemented Algorithms

## 3Sum

Find all unique triplets in an array that sum to zero.

Example:
```
three_sum([-1,0,1,2,-1,-4])
```

Output:
```
[[-1,-1,2],[-1,0,1]]
```


Time complexity:

$$
O(n^2)
$$

using sorting and two pointers.

---

## 0/1 Knapsack

Given weights and values of items, determine the maximum achievable value without exceeding capacity.

Dynamic programming recurrence:

$$
dp[i][w] =
\max(dp[i-1][w],\ v_i + dp[i-1][w-w_i])
$$

Time complexity:

$$
O(nW)
$$

where:

- $n$ — number of items
- $W$ — knapsack capacity.

---

## Coin Change

Compute the minimum number of coins required to form a target amount.

DP formulation:

$$
dp[i] = \min(dp[i], dp[i - coin] + 1)
$$

Time complexity:

$$
O(n \cdot amount)
$$

---

## Course Schedule II

Determine a valid order of courses given prerequisite relations.

Uses **topological sorting** (Kahn's algorithm).

Graph representation:

$$
b \rightarrow a
$$

meaning course $b$ must be taken before $a$.

Time complexity:

$$
O(V + E)
$$

---

## Course Schedule III

Schedule the maximum number of courses given durations and deadlines.

Algorithm:

1. sort by deadline
2. maintain max-heap of durations
3. drop the longest course when necessary.

Time complexity:

$$
O(n \log n)
$$

---

## Maximum Bomb Detonation

Each bomb can trigger other bombs within its radius.

The problem reduces to **graph reachability**.

For each node we run BFS:

$$
O(n^2)
$$

---

## Merge k Sorted Lists

Merge multiple sorted linked lists into one sorted list using a **min-heap**.

Time complexity:

$$
O(N \log k)
$$

where:

- $N$ — total number of nodes
- $k$ — number of lists.

---

## Minimum Cost to Move Chips

Observation:

- moves of distance 2 cost $0$
- moves of distance 1 cost $1$

Thus the answer is:

$$
\min(\text{even positions},\ \text{odd positions})
$$

---

## Number of Submatrices with Target Sum

Algorithm:

1. fix two rows
2. compress columns
3. count subarrays with prefix sums.

Time complexity:

$$
O(rows^2 \cdot cols)
$$

---

## Minimum Swaps to Group Balls

Count **inversions**:

$$
(1,0)
$$

Each inversion requires at least one swap.

Time complexity:

$$
O(n)
$$

---

## Unique Paths

Dynamic programming on grid.

Recurrence:

$$
dp[i][j] = dp[i-1][j] + dp[i][j-1]
$$

Time complexity:

$$
O(mn)
$$

---

# Running the Code

Most files include **doctests**.

Run tests:
```
python file_name.py
```


Example:
```
python three_sum.py
```


---

# Purpose of the Repository

This repository was created to practice:

- algorithm design
- data structures
- Python problem solving
- interview preparation.
