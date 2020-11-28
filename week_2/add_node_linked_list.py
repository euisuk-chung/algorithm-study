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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)

        # 0일때 index가 -1가 들어가는 것을 방지하기 위해
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

print('BEFORE')
linked_list = LinkedList(5)
linked_list.append(15)
linked_list.append(20)
linked_list.print_all() # 5 -> 12 -> 8

print('AFTER')
linked_list.add_node(1, 10)
linked_list.print_all()