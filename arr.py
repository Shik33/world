# your code goes here
class Node:
	def __init__(self, key):
		self.key = key
		self.next = None


class LinkedList:
    def __init__(self):
    	self.head = None

    def printList(self):
            temp = self.head
            while (temp):
                print (temp.key),
                temp = temp.next

if __name__ == '__main__':
	llist = LinkedList()
	
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	forth = Node(4)

	llist.head.next = second;
	second.next = third;
	third.next = forth;

llist.printList()