# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and locate the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Handle cases where k >= length
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect tail to head to form a circular structure
        tail.next = head
        
        # 4. Find the new tail node (at position length - k)
        new_tail_steps = length - k
        new_tail = head
        for _ in range(new_tail_steps - 1):
            new_tail = new_tail.next
            
        # 5. Break the ring and establish the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
    