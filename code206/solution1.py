# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList( self , headNode : ListNode ) -> ListNode :
        prev , cur = None , headNode
        while cur is not None:
            print(cur)
            next = cur.next     # 保存当前节点的Next
            cur.next = prev     # Next 节点指向上一节点
            prev = cur         # 下一节点
            cur = next
        return prev



