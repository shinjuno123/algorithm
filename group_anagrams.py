strs = ["eat","tea","tan","ate","nat","bat"]

# count is about how many times you found anagrams.
# ifthis value equals to length of strs, then "while" phrase has to be ended
count: int = 0
# current index number to find anagrams
current_idx: int = 0
while count <= len(strs):
    letters = list(strs[current_idx])
    for str_ in letters:
        if list(str_) in letters:
            print(str_, letters)
            count += 1





# print(if strs2[1] in strs1 else False)