# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])

        # print(heap)

        while heap:
            val, index = heapq.heappop(heap)
            curr.next = lists[index]
            curr = curr.next

            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, [lists[index].val, index])

        return dummy.next

        