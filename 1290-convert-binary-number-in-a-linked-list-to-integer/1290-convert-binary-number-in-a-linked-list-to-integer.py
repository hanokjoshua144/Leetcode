# Definition for singly-linked list.
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        curr = head

        while curr:
            num = num * 2 + curr.val
            curr = curr.next

        return num