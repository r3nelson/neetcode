# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case
        if not head or not head.next:
            return head
        
        # recursive call
        prev = self.reverseList(head.next)
        # take the next, next value and point it to the head. (reverse the order)
        head.next.next = head # e.g., head = 4 head.next = 5  4->5-> null  now 4-> 5 -> 4 (we reversed 5 from pointing at null to pointing at 4)
        # take current head and point it to nothing
        head.next = None # e.g., head = 4->5 now head = 4-> null
        return prev # prev = 5-> 4-> null
    

            
            
            
