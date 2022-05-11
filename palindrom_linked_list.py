# my way
# from collections import deque 
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         is_pal = True
#         nums = deque()
        
#         if not head:
#             return is_pal
        
        
#         while head is not None:
#             nums.append(head.val)
#             head = head.next
        
#         while len(nums) > 1:
#             if nums.pop() != nums.popleft():
#                 is_pal = False
        
#         return is_pal

# fancy way

