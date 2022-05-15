class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

def mergeTwoLists2(list1, list2):
    # cur과 dummy에 ListNode를 담는다.
    cur = dummy = ListNode()
    # 리스트노드1과 2가 두 개 모두 존재 하는 동안
    while list1 and list2:
        # 리스트1 값 과 리스트 2 값을 비교
        if list1.val < list2.val:
            # 리스트 1값이 작으면
            # cur에 다음 값에 리스트노드1을 넣는다.
            cur.next = list1
            #다음 노드를 현재 놓드에 넣고 현재노드를 cur에 넣는다.
            list1, cur = list1.next, list1
        else:
            # 리스트 2 값이 작거나 같으면
            # cur에 다음 값에 리스트노드2를 넣는다.
            cur.next = list2
            # 다음 노드를 현재 놓드에 넣고 현재노드를 cur에 넣는다.
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next

l1 = ListNode()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = ListNode()
for num in [1,2]:
    l2.append(num)

mergeTwoLists2(l1,l2)


# 이해하기 쉬운 풀이
def mergeTwoLists(list1, list2):
    if (list1 == None and list2 == None): return None
    head = result = ListNode()

    while (list1 or list2):
        if (list1 == None):
            result.val = list2.val
            result.next = list2.next
            break
        if (list2 == None):
            result.val = list1.val
            result.next = list1.next
            break
        else:
            if (list1.val <= list2.val):
                result.val = list1.val
                result.next = ListNode()
                result = result.next
                list1 = list1.next
            else:
                result.val = list2.val
                result.next = ListNode()
                result = result.next
                list2 = list2.next

    return head