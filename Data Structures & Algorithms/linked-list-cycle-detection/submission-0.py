# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_map = {}

        while head and head.next:
            if head in seen_map:
                return True
            else:
                seen_map[head] = head.next
                head = head.next
        
        return False
        