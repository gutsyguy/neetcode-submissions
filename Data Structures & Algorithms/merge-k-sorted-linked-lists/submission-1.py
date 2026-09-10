# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        curr = dummy = ListNode(0)

        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, i))

        
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = lists[idx]
            curr = curr.next
            lists[idx] = lists[idx].next

            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))

        return dummy.next
