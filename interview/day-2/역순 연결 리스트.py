class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head) -> ListNode:
    # SOL 1) Recursive Way
    def reversef(node, prev=None):
        if not node:
            # node가 비어있는 경우
            return prev
        next, node.next = node.next, prev
        return reversef(next, node)

    return reversef(head)


def reverseList(head):
    node, prev = head, None

    while node:  # 1 2 3

        next = node.next  # 2 3
        node.next = prev  # Null 1

        prev = node  # 1 2
        node = next  # 2 3


    return prev