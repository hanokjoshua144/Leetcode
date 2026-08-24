class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                value = curr.val

                while curr and curr.val == value:
                    curr = curr.next

                prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return dummy.next