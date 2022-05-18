# # 파이썬의 딕셔너리는 오픈 어드레싱을 사용한다.
# # 개별 체이닝 방식으로 구현해보자
# import collections
#
#
# class ListNode:
#     def __init__(self, key=None, value=None):
#         self.key = key
#         self.value = value
#         self.next = None
#
# class MyHashMap:
#     def __init__(self):
#         self.size = 1000
#         self.table = collections.defaultdict(ListNode)
#
#     def put(self, key: int, value: int) -> None:
#         index = key % self.size
#         # 인덱스 노드가 없다면 삽입 후 종료
#         if self.table[index].value is None:
#             self.table[index] = ListNode(key, value)
#             return
#
#         # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
#         p = self.table[index]
#         while p:
#             if p.key == key:
#                 p.value
#
#     def get(self, key:int) -> int:
#
#
#     def remove(self, key:int) -> None:
