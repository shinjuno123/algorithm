# create nodes
# create linked list
# add nodes to linked list
# print linked list




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next

        return length


    def insert(self, newNode):
        # head -> john -> None
        if self.head is None:
            self.head = newNode
        else:
            # head -> john -> Ben -> None || John -> Matthew
            # self.head.next = newNode

            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            
            lastNode.next = newNode
    
    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        # head -> mary -> john -> ben -> Matthew -> None || newNode -> hey -> None
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1



    def printList(self):
        # head -> john -> Ben -> Matthew -> None
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data,end = ' ')
            currentNode = currentNode.next

    def deleteAt(self,position):
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return

        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return

            currentNode = self.head
            currentPosition = 0

            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break

                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1



    def insertHead(self, newNode):
        # data -> Matthew , next -> None
        temporaryNode = self.head # John
        self.head = newNode # Mary
        self.head.next = temporaryNode # Mary -> John
        del temporaryNode

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        
        previousNode.next = None
    
    def isListEmpty(self):
        return self.head is None



# Node -> data, next
# firstNode.data -> John, firstNode.next -> None
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insert(thirdNode)
fourthNode = Node("Mary")
linkedList.insertHead(fourthNode)
fifthNode = Node("hey")
linkedList.printList()
print()
linkedList.insertAt(fifthNode,2)
linkedList.printList()
print()
linkedList.deleteEnd()
linkedList.deleteEnd()
linkedList.deleteEnd()
linkedList.deleteEnd()

linkedList.printList()
print()
linkedList.deleteAt(0)
linkedList.printList()
print()