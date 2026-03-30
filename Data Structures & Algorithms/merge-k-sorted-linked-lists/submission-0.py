# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: # If Null or empty list is passed in
            return None
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                L1 = lists[i]
                L2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.merge_list(L1, L2))
            lists = merged_list
        return lists[0]

    def merge_list(self, L1, L2):
        dummy = node = ListNode()
        while L1 and L2:
            if L1.val < L2.val:
                node.next = L1
                L1 = L1.next
            else:
                node.next = L2
                L2 = L2.next
            node = node.next
        node.next = L1 or L2
        return dummy.next

