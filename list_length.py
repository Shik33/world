class Node: 
    def __init__(self, key):
        self.key = key
        self.next = None
class LinkedList:
    def __init__head(self):
        self.head = None

    def printCount(self):
        temp = self.head
        count = 0

        while (temp):
            print (temp.key)
            count = count + 1
            temp = temp.next
        print (count)

if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(8)
    
    llist.head.next = second;
    second.next = third;
    third.next = forth;
    forth.next = fifth;

llist.printCount()