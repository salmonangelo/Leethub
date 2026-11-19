# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            
            
            gcd = 1
            max_val = max(curr.val,curr.next.val)
            min_val = min(curr.val,curr.next.val)

            while max_val%min_val:
                gcd = max_val%min_val
                max_val = min_val
                min_val = gcd

            gcd_node = ListNode(min_val)
            temp = curr.next
            curr.next = gcd_node
            gcd_node.next = temp
            curr = temp


        
        return head