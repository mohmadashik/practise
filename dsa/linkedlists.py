class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None
class SingleLinkedList:
    
    def __init__(self,node):
        self.head = node 

    def append(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def display_all(self):
        current = self.head 
        while current:
            print(current.val,end='->')
            current = current.next 
        print('None')
    

    def detect_cycle(self):
        slow = self.head 
        fast = self.head 

        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast :
                return True
        
        return False 
linkedlist = SingleLinkedList(Node(10))


linkedlist.append(20)
linkedlist.append(30)
linkedlist.append(40)
linkedlist.append(50)
linkedlist.append(60)
linkedlist.display_all()

print('detect cycle : ',linkedlist.detect_cycle())

linkedlist.head.next.next.next.next = linkedlist.head.next

print('detect cycle : ',linkedlist.detect_cycle())

