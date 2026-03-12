"""Exercise 1 from LeetCode"""

def coin_change(coins: list[int], amount: int) -> int:
    """
    >>> coin_change([186,419,83,408], 6249)
    20
    """

    #dp[i] буде означати мінімальну кількість монет, щоб скласти суму i.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 #базовий випадок, об скласти суму 0, не потрібно жодної монети

    for i in range(1, amount + 1): #перебір сум від 1 і до amount
        for coin in coins:
            if i - coin >= 0: #Перевірка, чи можна використати монету
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]

#     if amount == 0:
#         return 0

#     counter = 0
#     sorted_coins = sorted(coins, reverse=True)
#     indxx = 0

#     while True:
#         amount -= sorted_coins[indxx]
#         if amount == 0:
#             counter += 1
#             return counter
#         if amount > 0:
#             counter += 1
#         elif amount < 0:
#             amount += sorted_coins[indxx]
#             if indxx + 1 < len(coins):
#                 indxx += 1
#             else:
#                 return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
