# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        lst = []
        node = head
        while node:
            lst.append(node.val)
            node = node.next

        lst = sorted(lst)

        rtn = ListNode(lst[0])
        for i in range(1, len(lst)):
            node = rtn
            while node.next:
                node = node.next

            node.next = ListNode(lst[i])

        return rtn
