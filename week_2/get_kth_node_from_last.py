class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

# solution 1 : 전체 길이 반환 후 해당 위치 인덱스 조회
#     def get_kth_node_from_last(self, k):
#         # list 길이 추출
#         length = 1
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#             length += 1
#
#         # 위치 반환
#         end_length = length - k
#         cur = self.head
#         for i in range(end_length):
#             cur = cur.next
#         return cur

# solution 2 : K 차이나는 노드들을 동시에 이동시키는 방법론
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)