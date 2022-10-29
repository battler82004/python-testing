# James Taddei
# Reverse Linked List
# 10/29/22

class LinkedNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
        
    def append(self, value):
        newNode = LinkedNode(value)
        curr = self.head
        if (not self.isEmpty()):
            while (curr.next != None):
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode
            
    def output(self):
        curr = self.head
        while (curr.next != None):
            print(curr.val,end=" ")
            curr = curr.next
        print(curr.val)
        
    def reverse(self):
        prev = None
        curr = self.head
        
        while (curr is not None):
            # Change curr
            next = curr.next
            curr.next = prev
            # Update vars
            prev = curr
            curr = next
        self.head = prev
        
def main():
    # Create linked list
    linked = LinkedList()
    linked.append(1)
    linked.append(2)
    linked.append(3)
    linked.output()
    
    # Reverse
    linked.reverse()
    linked.output()
    
if (__name__ == "__main__"):
    main()