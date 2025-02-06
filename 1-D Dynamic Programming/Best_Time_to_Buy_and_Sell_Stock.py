# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# DP

def maxProfit(prices):
    maxP = 0
    minBuy = prices[0]

    for sell in prices:
        maxP = max(maxP, sell - minBuy)
        minBuy = min(minBuy, sell)

    return maxP

print(maxProfit([7,1,5,3,6,4]))


# Two Pointers

def maxProfit(prices):

    l, r = 0, 1

    maxP = prices[0]

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        
        else:
            l = r
        r += 1

        return maxP