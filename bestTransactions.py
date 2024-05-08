from typing import List

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time.
You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    ######## my Solution : O(n) ##############
    def my_maxProfit(self, prices: List[int]) -> int:

        # do one scan to retrieve max single Transaction
        mb = 0
        ms = 1

        singleTrans = 0
        while mb != len(prices)-2 and ms != len(prices)-1:
            while ms+1 < len(prices) and prices[ms+1] > prices[ms]:
                ms += 1
            while mb+1<ms and prices[mb+1] < prices[mb]:
                mb += 1
            singleTrans = max(singleTrans, prices[ms] - prices[mb])

            if ms+1 < len(prices):
                ms += 1
            if mb+1 < ms:
                mb += 1

        # examine two Transactions option:
        mb1 = 0
        ms1 = 1
        mb2 = 2
        ms2 = 3
        twoTrans = 0
        firstTrans = prices[ms1] - prices[mb1]
        secTrans = prices[ms2] - prices[mb2]
        while mb1 < len(prices)-3 and ms1 < len(prices)-2 and mb2 < len(prices)-1 and ms2 < len(prices):
            currTrans = firstTrans + secTrans
            #twoTrans = max(twoTrans, currTrans)

            if ms2-mb2 == mb2-ms1 == ms1-mb1 == 1: #stuck situation
                ms2 += 1

            while ms2 < len(prices)-1 and prices[ms2+1] >= prices[ms2]:
                ms2 += 1

            while mb2+1 < ms2 and prices[mb2+1] <= prices[mb2]:
                mb2 += 1
            # record best second trans and advance
            secTrans = prices[ms2] - prices[mb2]
            twoTrans = max(twoTrans, firstTrans + secTrans)
            ms2 += 1
            mb2 += 1

            while ms1+1 < mb2 and prices[ms1+1] >= prices[ms1]:
                ms1 += 1

            while mb1+1 < ms1 and prices[mb+1] <= prices[mb1]:
                mb1 += 1
            # record best first trans and advance
            firstTrans = prices[ms1] - prices[mb1]
            twoTrans = max(twoTrans, secTrans + firstTrans)
            if ms1 < mb2 - 1:
                ms1 += 1
            if mb1 < ms1 - 1:
                mb1 += 1


        return max(singleTrans, twoTrans)



sol = Solution()
prices = [100, 30, 15, 10, 8, 25, 80]
print(sol.my_maxProfit(prices))

