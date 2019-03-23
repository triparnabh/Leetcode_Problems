class Solution(object):
    def detectCycle(self, head):

        s = set()
        if not head:
            return None
        while (head):
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None
