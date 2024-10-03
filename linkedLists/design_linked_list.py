class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.length = 0

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:        
        if index > self.length:
            return -1
        
        cur = self.head.next
        
        while index >= 0 and cur!= self.tail:
            cur = cur.next
            index -= 1

        return cur.val 

    def addAtHead(self, val: int) -> None:

        newNode = ListNode(val)

        if self.length == 0:
            self.head.next = newNode
            self.tail.prev = newNode
            newNode.prev = self.head
            newNode.next = self.tail
        

        prev,next = self.head, self.head.next
        next.prev = newNode
        prev.next = newNode
        newNode.next = next
        newNode.prev = prev

        self.length+= 1
        
        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        if self.length == 0:
            self.head.next = newNode
            newNode.prev = self.head
            self.tail.prev = newNode

        prev,next = self.tail.prev, self.tail
        next.prev = newNode
        prev.next = newNode
        newNode.next = next
        newNode.prev = prev

        self.length+= 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        
        if index == self.length:
            self.addAtTail(val)

        if index == 0:
            self.addAtHead(val)

        newNode = ListNode(val)

        cur = self.head.next
        while index > 0:
            cur = cur.next
            index -= 1
        
        prev, next = cur.prev, cur.next
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev

        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        cur = self.head.next
        while index > 0 and cur!= self.tail:
            cur = cur.next
            index -= 1
        
        prev, next = cur.prev, cur.next
        next.prev = prev
        prev.next = next

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)