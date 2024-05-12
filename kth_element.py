
from typing import Optional, Dict, List

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        l = 0
        r = len(nums) - 1
        return self.rand_select(nums, len(nums) - k + 1, l, r)

    def rand_select(self, nums: List[int], k: int, l, r):
        curr_rank = self.partition(nums, l, r)
        if curr_rank == k - 1:
            return nums[curr_rank]
        elif curr_rank > k-1:
            return self.rand_select(nums, k, l, r-1)
        elif curr_rank < k-1:
            return self.rand_select(nums, k, l+1, r)


    def partition(self, nums: List[int], l, r):

        if l==r:
            return r

        e = l
        l = l + 1
        while True:
            while nums[r] > nums[e]:
                r -= 1
            while nums[l] < nums[e]:
                l += 1
            if l < r:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                r -= 1
                l += 1
            else:
                temp = nums[r]
                nums[r] = nums[e]
                nums[e] = temp
                return r


nums = [3,2,3,1,2,4,5,5,6]
k = 4
sol = Solution()
print(sol.findKthLargest(nums,k))