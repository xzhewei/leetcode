# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        next_node = head.next    #        head -> next_node 
        next_node.next = head    #        head <- next_node 
        head.next = None         # [x] <- head <- next_node 
        return new_head

