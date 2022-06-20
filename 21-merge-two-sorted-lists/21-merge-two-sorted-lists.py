# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        mergedList = ListNode()
        currentNode = mergedList
        
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                currentNode.val = list1.val
                list1 = list1.next
                
            else:
                currentNode.val = list2.val
                list2 = list2.next
            
            if list1 or list2:
                currentNode.next = ListNode()
                currentNode = currentNode.next

        return mergedList