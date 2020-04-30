# https://leetcode.com/problems/add-two-numbers
'''
Approach: Traverse both lists and One by one pick nodes of both lists and add the values.
If the sum is more than 10 then make carry as 1 and reduce sum.
If one list has more elements than the other then consider remaining values of this list as 0.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = temp = ListNode(0)
        while l1 or l2 or carry:
            v1=v2=0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            currsum = v1+v2+carry
            carry,val =  currsum//10 , currsum%10
            temp.next = ListNode(val)
            temp = temp.next
        return head.next