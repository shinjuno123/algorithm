# my way 56ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str to list
        s_list = list(s)
        s_only_alpha: str = ''
        # load each element of list to str variable
        for s in s_list:
            if s.isalnum():
                s_only_alpha += s.lower()
        # reverse the first list
        s_list_reversed = list(reversed(s_list))
        s_only_alpha_reversed: str = ''
        # load each element of the reversed list to str variable
        for s in s_list_reversed:
            if s.isalnum():
                s_only_alpha_reversed += s.lower()
        # compare if s_only_alpha_reversed is same with s_only_alpha
        if s_only_alpha == s_only_alpha_reversed:
            return True
        else:
            return False


print(Solution.isPalindrome(None, 'A man, a plan, a canal: Panama'))


# in the book 245ms
# 여기서는 O(n^2)의 시간복잡도가 나온다.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:  # O(n)
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:  # O(n)
            if strs.pop(0) != strs.pop():  # pop(0) -> O(n)
                return False

        return True


print(Solution.isPalindrome(None, 'A man, a plan, a canal: Panama'))

# 데크를 명시적으로 선언하면 더욱 속도를 높일 수 있다. 56ms
# 데크의 popleft()는 O(1)이고 리스트의 pop(0)는 O(n)이기 때문이다.
# O(n)의 시간복잡도가 나온다.
import collections
from collections import deque as Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():  # O(n)
                strs.append(char.lower())

        while len(strs) > 1:  # O(n)
            if strs.popleft() != strs.pop():  # O(1)
                return False

        return True


print(Solution.isPalindrome(None, 'A man, a plan, a canal: Panama'))

# 슬라이싱을 활용하면 더 빠르게 할 수 있다.
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)  # 정규 표현식과 일치하는 것에 대해서 다른 문자열로 대체한다.
        # [^]이것 괄호안 웃음 표시는 해당문자를 제외한 문자를 매칭한다는 것이다. 즉 알파벳과 숫자를 제외한 문자들은 ('')지우라는 의미가 된다.

        return s == s[::-1]


print(Solution.isPalindrome(None, 'A man, a plan, a canal: Panama'))
