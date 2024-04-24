from heapq import heappop, heappush
import random
'''
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
'''
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

## left to the median there is max heap (root of it is the closest element to the median)
## max_heap is obtained by -1 mult !
## right to the median there is min heap (root of it is the closest element to the median or the median itself)
    def addNum(self, num: int) -> None:

        if(len(self.max_heap) == 0 and len(self.min_heap) == 0):
            heappush(self.min_heap, num)
            return

        if len(self.max_heap) != 0 and num >= -1 * self.max_heap[0]: # num is bigger than median or the median itself --> deserve a place in min_heap
            heappush(self.min_heap, num)
        elif len(self.min_heap) != 0 and num < self.min_heap[0]:
            heappush(self.max_heap, -1*num)

        diff = len(self.max_heap) - len(self.min_heap) ## always balance the heaps. if even number of elements --> median is the root of min_heap

        if diff == -2:
            heappush(self.max_heap, -1 * heappop(self.min_heap))
        elif diff == 1:
            heappush(self.min_heap, -1 * heappop(self.max_heap))

        return
    def findMedian(self):

        if len(self.min_heap) == 0:
            return None
        elif len(self.max_heap) == len(self.min_heap):
            return (-1*self.max_heap[0] + self.min_heap[0])/2
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
commands_list = ["MedianFinder", "addNum"]
for i in range(0, 15):
    command = random.choice(commands_list)
    print("**********command is:********** ", command)
    if command == "addNum":
        num = random.randint(-12, 10)
        print("add num of:", num)
        obj.addNum(num)
    if command == "MedianFinder":
        median = obj.findMedian()
        if median == None:
            print("find median:" + "\n" + " median is: []")
        else:
            print("find median:" + "\n" + " median is: {:.2f}".format(median))

