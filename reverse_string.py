# 파이써닉한 방식
s = list("hello")
s.reverse()
print(s)



# 전통적인 투 포인터 방식

s = list("hello")
left = 0
right = len(s)-1

while left != right:
    s[left],s[right] = s[right],s[left]
    left += 1
    right -= 1

print(s)


