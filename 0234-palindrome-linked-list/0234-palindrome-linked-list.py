class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare first half and reversed second half
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True



        