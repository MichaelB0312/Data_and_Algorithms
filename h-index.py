from typing import List
'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper,
 return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that
 the given researcher has published at least h papers that have each been cited at least h times.
 Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000

 Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
'''
# based on part of counting sort. Time Complexity: O(n+1000)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 1000*[0] #each idx represent number of citations. each cell consists number of papers
        for i in range(len(citations)):
            count[citations[i]] += 1

        # now each count[i] will contain number of papers with at least i citations:
        # find the maximal h through it
        h_max = 0
        for i in range(998, -1, -1):
            count[i] += count[i+1]
            h_max = max(h_max, min(i, count[i]))

        return h_max



sol = Solution()
citations = [1,3,1]
print(sol.hIndex(citations))
