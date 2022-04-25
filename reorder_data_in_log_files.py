logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

letter_logs = []
digit_logs = []

key = 0
for log in logs:
    if log.split(' ')[1].isdigit():
        digit_logs.append(log)
    else:
        letter_logs.append(log)


def splitProcess(x):
    return x.split()[1:], x.split()[0]  # contents, identifier


# letter_logs.sort(key=splitProcess)
letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

print(letter_logs + digit_logs)
# 여기서 중요한 것은 sort에서 key 매개변수에 대해서 def나 lambda를 사용했을 때 return을 정렬되기 원하는 우선순위로 지정할 수 있다는 것이다.

