class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
node = Node(3)  # 현재는 next 가 없이 하나의 노드만 있습니다. [3]
first_node = Node(4) # 현재는 next 가 없이 하나의 노드만 있습니다. [4]
second_node = Node(5) # [5] 를 들고 있는 노드를 만듭니다.

# 관계 정의
node.next = first_node
first_node.next = second_node

print(node.data) #node
print(node.next.data) #first_node
print(node.next.next.data) #second_node


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

    def append(self, value):     # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        cur = self.head
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다.
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

print("linked_list")
linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()