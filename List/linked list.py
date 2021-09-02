# Node class
class Node:

    # function to initialize node object
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:

    # Initialize the linked list with head pointing to null
    def __init__(self):
        self.head = None

    # print the list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Add new node in front
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # add node after a specific node
    def insertAfter(self, prev_node, new_node):
        if prev_node is None:
            print("The node must be linkedlist")
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

    # add node at the end
    def append(self, new_data):
        new_node = Node(new_data)

        # if the linked list is empty, make the new node as the head
        if self.head == None:
            self.head = new_node
            return

        # traverse until we reach the last node
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node
    
    # delete node with specific "key"   
    def deleteNode(self, key):
        temp = self.head

        # check if value of head is equal to key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
            while(temp is not None):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next

            if temp == None:
                print(f"Node with {key} doesn't exist")
                return

            prev.next = temp.next
            temp = None
            

    # Delete a Linked List node at a given position
    def deleteNodePos(self, pos):

        # if the linked list is empty
        if self.head == None:
            print("Empty Linked List")
            return

        # if head needs to be removed
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            print("Linked list after deletion operation")
            self.printList()
            return

        p = 0
        while(p != pos):
            prev = temp
            temp = temp.next
            if temp == None:
                print("Position index out of range")
                return
            p += 1


        prev.next = temp.next
        temp = None

        print("Linked list after deletion operation")
        self.printList()

    # Count the number of nodes in linked list
    # iterative appproach
    def countNodes(self):
        temp = self.head
        count = 0
        if temp == None:
            return 0

        while(temp is not None):
            temp = temp.next
            count += 1

        return count

    # Count the number of nodes in linked list
    # iterative appproach
    def countNodesRecur(self, node):
        if not node:
            return 0
        else:
            return 1 + self.countNodesRecur(node.next)

    def countNodesRecursion(self):
        return self.countNodesRecur(self.head)


llist = LinkedList() # initialized an empty linked list
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.printList()
llist.push(5)
llist.printList()
llist.append(10)
llist.append(20)
llist.printList()