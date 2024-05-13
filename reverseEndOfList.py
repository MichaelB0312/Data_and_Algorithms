from typing import Optional, List

'''
Given the head of a linked list, rotate the list to the right by k places.
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int):
        tail = head

        while tail.next != None:
            tail = tail.next

        # make circular list
        tail.next = head

        tail = head
        prev = head
        for _ in range(k+1):
            prev = tail
            tail = tail.next

        head = tail
        prev.next = None

        self.printList(head)

    def printList(self, head: Optional[ListNode]):
        out_list = []
        while head != None:
            out_list.append(head.val)
            head = head.next

        return print(out_list)

    def buildList(self, inputList: List[int]) -> Optional[ListNode]:

        head = ListNode(val=inputList[0])
        curr_node = head
        for i in range(1, len(inputList)):
            head.next = ListNode(val=inputList[i])
            head = head.next

        return curr_node


head = [0,1,2]
k = 4
sol = Solution()
head = sol.buildList(head)
sol.rotateRight(head, k)