# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
            Understand:
                - I have to rearrange the linked list in the order
                [0, n-1, 1, n-2, 2, n-3, ....]
                - I can't change the values of the list node. 
            Plan:
                - Reverse the linked list and then create a new linked_list utilizing
                the values until both the normal and reversed linked lists reach the same
                value. (Ignore the first element)
        """
        fast = head
        slow = head
        curr = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

            


        