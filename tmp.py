# linked list
# insert, inserthead, insertat, printlist, listlength

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    
    def length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
    
    def insertHead(self,new_node):
        tmp_node = self.head
        self.head = new_node
        self.head.next = tmp_node
        del tmp_node
    
    def insertEnd(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head

            while last_node.next is not None:
                last_node = last_node.next
            
            last_node.next = new_node
    
    def printLinkedList(self):
        current_node = self.head

        while current_node is not None:

            print(current_node.val,end=' ')
            current_node = current_node.next

        print()

    def insertAt(self, new_node, position):
        if position < 0 or position > self.length():
            return

        if position == 0:
            self.insertHead(new_node)
            return

        current_node = self.head
        position_number = 0
        while True:
            if position_number == position:
                previous_node.next = new_node
                new_node.next = current_node
                break

            previous_node = current_node
            current_node = current_node.next
            position_number += 1
    
    def deleteEnd(self):
        last



nums = [5,4,3]
linked_list = LinkedList()
for num in nums:
    node = Node(num)
    linked_list.insertEnd(node)
linked_list.printLinkedList()

node = Node(7)
node1 = Node(7)
node2 = Node(222)
linked_list.insertHead(node)
linked_list.insertHead(node1)
linked_list.insertAt(node2,5)
linked_list.printLinkedList()