strs = ["dddddg","ggggd"]

# wrong...
# count is about how many times you found anagrams.
# if this value equals to length of strs, then "while" phrase has to be ended
# count: int = 0
# current index number to find anagrams

def checkAnagrams(str_,letters):
    # if length is same
    letter_cnt = 0
    if len(str_) == len(letters):
        for letter in list(str_):
            if  letter in letters:
                letter_cnt += 1
        if letter_cnt ==  len(letters):
            return True
        else:
            return False
    else:
        return False


result = []
current_idx: int = 0
used_idc = set()
while current_idx < len(strs):
    # print(current_idx)
    if current_idx not in used_idc:
        letters = list(strs[current_idx])
        used_idc.add(current_idx)
        # letters ['e','a','t']
        local_result = []
        for i,str_ in enumerate(strs): # str_ -> 'eat'
            # print(letters in list(str_))
            if checkAnagrams(str_,letters): #list(str_) -> ['e','a','t'] in letters ['e','a','t']
                # print(str_, letters)
                used_idc.add(i) # add checked index
                local_result.append(str_)
                # print(used_idc)
        result.append(local_result)
        local_result = []
    current_idx += 1
print(result)


# print(if strs2[1] in strs1 else False)
# true answer
import collections

anagrams = collections.defaultdict(list)
# print(anagrams)

for word in strs:
    # 정렬하여 딕셔너리에 추가
    # eat -> aet, tea -> aet ----> {'aet':[eat,tea]}
    anagrams[''.join(sorted(word))].append(word)

# print(anagrams)
print(list(anagrams.values()))