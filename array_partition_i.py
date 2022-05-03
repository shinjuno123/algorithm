# my way 1

nums = [6,2,6,5,1,2]

nums.sort()
result: int = 0

for i in range(0,len(nums)-1,2):
    result += min(nums[i],nums[i+1])

print(result)

# book way

nums.sort()
pair = []
result :int = 0
for n in nums:
    pair.append(n)
    if len(pair) == 2:
        result += min(pair)
        pair = []
    
print(result)

# my way 2

nums.sort()
result: int = 0

for i in range(0,len(nums)-1,2):
    result += nums[i]

print(result)


# book way 2
nums.sort()
result: int = 0

for i,v in enumerate(nums):
    
    if i % 2 == 0:
        result += v

print(result)

# pythonic way
nums.sort()
print(sum(nums[::2]))