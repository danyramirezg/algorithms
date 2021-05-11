#!/usr/bin/bash/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):

    if head is None:
        return

    current = head
    count = 1

    while current.next is not None:
        current = current.next
        count += 1
    return count

def print_linked_list(head):

    current = head

    while current.data is not None:
        current.data
        current.next
        print(current.data)

head = Node(6)
node2 = Node(3)
node3 = Node(4)

head.next = node2
node2.next = node3

print("The linked list's length is: ", end="")
print(count_nodes(head))
