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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # initialize sum value
    sum1 = 0
    sum2 = 0
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head

    # loop 1
    while cur1 is not None:
        sum1 += cur1.data
        cur1 = cur1.next

    # loop 2
    while cur2 is not None:
        sum2 += cur2.data
        cur2 = cur2.next

    total_sum = sum1 + sum2

    return total_sum #1032


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(4)
linked_list_2.append(5)

# 3+4+5+6+7+8 =33

print(get_linked_list_sum(linked_list_1, linked_list_2))