class Node:
    def __init_＿(self, value):
        self.value = value
        self.next = None
        self.prev = None

#創建雙向列表 構造器
class DoublyLinkedList:
    def __iniit__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while self.head:
            while temp is not None:
                print(temp.value)
                temp = temp.next

my_doubly_linked_list = DoublyLinkedList(7)

my_doubly_linked_list.print_list()