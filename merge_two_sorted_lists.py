class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = [1,2,4]
list2 = [1,3,4]
node1 = None
for val in list1:
    node1 = ListNode(val)
    node1.next = node1

node2= None
for val in list2:
    node2 = ListNode(val)
    node2 = node2.next


while node2.next is not None:
    val = node2.val
    print(val)
    node2 = node2.next

from collections import deque



