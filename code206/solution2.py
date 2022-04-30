# Definition for singly-linked list.

# 思想明白，但还是有不熟练
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList( self , node : ListNode ) -> ListNode :
        if node is None or node.next is None:
            return node

        p = self.reverseList( node.next )
        node.next.next = node
        node.next = None

        return node
