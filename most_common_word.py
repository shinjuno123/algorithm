from collections import Counter
import re
# my way
paragraph_origin = "abc abc? abcd the jeff!"
banned = ["abc", "abcd", "jeff"]
special_case = ["!", "?", "'", ",", ";", "."]
result_list = []
paragraph = paragraph_origin.lower()
# remove all the special cases
for case in special_case:
    paragraph = paragraph.replace(case, ' ')
paragraph_list = paragraph.split()

for element in paragraph_list:
    if element not in banned:
        result_list.append(element)

counter = Counter(result_list).most_common(1)[0][0]




# True answer
# \w = word character(문자) ^ = not
words = [word for word in re.sub(r'[^\w]', ' ', paragraph_origin).lower().split() if word not in banned] # list comprehension
counts = Counter(words)
print(counts.most_common(1)[0][0])
