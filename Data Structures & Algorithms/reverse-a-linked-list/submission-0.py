# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        if head != None:
            temp_next = head.next
        

            while (current.next != None):
                temp_next = current.next
                current.next = prev
                prev = current
                current = temp_next
            
            temp_next = current.next
            current.next = prev
            prev = current
            
            return prev
        else:
            temp_next = None
            


        
            
        