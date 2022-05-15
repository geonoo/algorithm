class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)


def isPalindrome(head) -> bool:
    arr = []
    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node.next

    while len(arr) > 1:
        if arr.pop() != arr.pop(0):
            return False

    return True




l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1,2]:
    l2.append(num)

print(isPalindrome(l1.head))
print(isPalindrome(l2.head))