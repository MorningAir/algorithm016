class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        fast, slow = head.next, head
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
