class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddevenlist(self, head: ListNode) -> ListNode:

    if not head:
        return head

    odd = odd_root = head
    even = even_root = head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next

    odd.next = even_root

    return odd_root