# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy code to serve as the starting point for the merged list.
        # The dimmy node helps us avoid some special cases, like both lists being empty or one list being empty
        dummy = node = ListNode()

        # Continue iterarting while both lists have nodes
        while list1 and list2:

            if list1.val < list2.val:
                # If list1's node is smaller, link it to the merged list
                node.next = list1

                # move to the next node in list1
                list1 = list1.next
            
            else:
                
                node.next = list2

                list2 = list2.next
    
            node = node.next
        
        # If there are any nodes remaining from either list add them on
        node.next = list1 or list2

        # Returns the sorted list ignoring the extra node we added at the start
        return dummy.next
        
