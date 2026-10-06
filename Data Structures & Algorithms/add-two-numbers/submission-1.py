# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur, head = None, None, None
        carry = 0
        cur1, cur2 = l1, l2
        while cur1 != None or cur2 != None:
            cur1_val = 0
            if cur1 != None: 
                cur1_val = cur1.val

            cur2_val = 0
            if cur2 != None: 
                cur2_val = cur2.val

            val_sum = cur1_val + cur2_val + carry
            if val_sum > 9:
                carry = 1
            else:
                carry = 0
            
            cur = ListNode(val_sum % 10)
            if prev == None:
                head = cur
            else:
                prev.next = cur

            prev = cur
            if cur1 != None:
                cur1 = cur1.next
            if cur2 != None:
                cur2 = cur2.next
        
        if carry == 1:
            cur.next = ListNode(1)

        return head
    
