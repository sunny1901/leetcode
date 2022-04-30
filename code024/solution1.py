# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, node: ListNode) -> ListNode:
        if not node or not node.next:
            return node

        nextNode = node.next                            # 2 = 1
        node.next = self.swapPairs(nextNode.next)       # 1.next = (3)
        nextNode.next = node                            # 2.next = 1
        return nextNode                                 # 2


