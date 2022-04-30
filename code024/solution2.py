# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, node: ListNode) -> ListNode:
        dummyHead = ListNode(0)  # 生成一个模子
        dummyHead.next = node    # 模子.next =  node

        temp = dummyHead

        while temp.next and temp.next.next :


            node1 = temp.next                   #
            node2 = temp.next.next
            temp.next = node2                   # 上一单元.next 指向 node2 （和上一节说by）

            node1.next = node2.next
            node2.next = node1

            temp = node1            # 循环相关，算法无关
        return dummyHead.next


