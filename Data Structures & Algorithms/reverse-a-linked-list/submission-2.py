# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr != None:
            # This keeps track of what the next ListNode is
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        return prev

            
        

"""
0 -> 1 -> 2 -> 3
prev = 
curr = 0
curr.next = 2
temp = 1


"""