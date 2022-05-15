# linked list의 노드
class ListNode:
    def __init__(self, val, next=None):  # 노드가 가진 값: val, 내가 가르키는 값: next
        self.val = val
        self.next = next


class LinkedList:
    ## 처음엔 헤드에 아무것도 없다라는 의미
    def __init__(self) -> object:
        self.head = None

    # 차례로 넣기
    # linked list append
    def append_node(self, val):
        # 만약 헤드에 아무것도 없으면
        if not self.head:
            self.head = ListNode(val, None)
            return

        # 헤드가 있으면 노드를 연결하기 위해 계속 다음 노드를 가리킴
        node = self.head
        # 다음 노드가 있을 때까지 계속 넘어감
        while node.next:
            node = node.next

        # 마지막 까지 탐색한 노드의 다음에 노드를 붙임임
        node.next = ListNode(val, None)

    # 탐색
    # linked list의 idx에 해당하는 노드를 리턴함
    def get_node(self, idx):
        count = 0
        node = self.head
        while count < idx:
            count += 1
            node = node.next
        return node

    # 탐색 2
    # linked list idx 해당하는 노드의 값을 리턴
    def get_node_val(self, idx):
        count = 0
        node = self.head
        while count < idx:
            count += 1
            node = node.next
        return node.val

    # 탐색 3
    # linked list에 있는 모든 노드를 리스트로 턴
    def get_all_node(self):
        if not self.head:
            return []
        all_node = []
        node = self.head
        while node.next:
            all_node.append(node.val)
            node = node.next
        all_node.append(node.val)
        return all_node

    # 삽입
    # linked list의 idx에 val 값을 가진노드를 삽입! -> 맨뒤에 넣는게 아님
    def add_node(self, idx, val):
        # 처음엔 뒤에 아무 값도 없다고 가정!
        new_node = ListNode(val, None)
        # 인덱스가 0이면
        if idx == 0:
            # 맨 앞이므로 헤드를 뒤에 붙임!
            new_node.next = self.head
            # 그리고 head를 가리켜줌!
            self.head = new_node
            return
        # 삽입되어 왼쪽이 될 노드!
        left_node = self.get_node(idx - 1)
        # 삽입되어 오른쪽이 될 노드
        right_node = left_node.next
        # 왼쪽 노드에 새로 들어온 노드를 붙이고!
        left_node.next = new_node
        # 새로운 노드에 오른쪽 노드를 붙인다!
        new_node.next = right_node

    # 삭제
    def delete_node(self, idx):
        if idx == 0:
            self.head = self.head.next
            return
        # 삭제할 idx의 왼쪽 노드
        left_node = self.get_node(idx - 1)
        # 삭제할 idx의 오른쪽 노드
        right_node = left_node.next.next
        # 이어붙이기
        left_node.next = right_node


nums = [1, 2, 4, 5]
lnk = LinkedList()
# 노드에 차례로 값 넣기
for i in nums:
    lnk.append_node(i)

# 노드의 모든 값 리턴하기
print(lnk.get_all_node())

# 노드 사이에 값 넣기
# 2번째 인덱스에 3을 넣자
lnk.add_node(2, 3)
print(lnk.get_all_node())

# 노드값 확인
# 2번째 인덱스인 3을 가져와보자
print(lnk.get_node_val(2))

# 노드 삭제하기
# 2번째 인덱스인 3 삭제하기
lnk.delete_node(2)
print(lnk.get_all_node())
print(lnk.get_node_val(2))