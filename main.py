import sys

a: int = 1  # 변수의 값도 타입을 선언했다 하더라도 동적으로 할당되어지기 때문에 주의가 필요하다
b: int = 6


def fn(c: int) -> bool:  # 여기의 bool은 어떤 함수를 반환할지 적어준다, c : int에서는 int값을 입력으로 받는다는 의미이다.
    return c > 5  # bool이라고 타입힌트를 미리 설정하더라도 값은 동적으로 할당되기 때문에 주의가 필요하다.


print(fn(b))
print(a)

map_and_lambda = list(map(lambda x: x + 10, [1, 2, 3, 3, 3]))

# list Comprehension? 기존의 리스트를 기반으로 새로운 리스트를 만들어내는 구문이다.
list_comprehension = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(list_comprehension)


def get_natural_number() -> int:  # yield구문 : 제너레이터가 여태까지 실행 중이던 값을 내보낸다. 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다. 물론 while True문의 경우
    n = 0  # 종료조건이 없으므로 계속해서 값을 내보낼 수 있다.
    while True:
        yield n
        n += 1


g = get_natural_number()

for _ in range(0, 100):
    print(next(g), end=',')


def generator():
    yield 1
    yield 'string'
    yield True


g = generator()
print(next(g))
print(next(g))
print(next(g))

## range
print(list(range(5)))  # [0,1,2,3,4,5]
print(range(0, 5))  # range(0,5)
print(type(range(5)))  # <class 'range'>
for i in range(5):
    print(i, end=' ')  # 0 1 2 3 4

## generator(yield, range) vs list
a: list = [n for n in range(1000000)]
b: range = range(1000000)

print(len(a))  # 1000000
print(len(b))  # 1000000
print(b)  # range(0,1000000)
print(type(b))  # <class 'range'>
print(sys.getsizeof(a))  # 8697456
print(sys.getsizeof(b))  # 48
print(a[999])  # 999
print(b[999])  # 999

# enumerate
a: list = [1, 2, 3, 4, 5, 6, 45]
print(a)  # [1,2,3,4,5,6,45]
print(enumerate(a))  # <enumerate object at 0xxxxxxx>
print(list(enumerate(a)))  # [(0,1),(1,2),(2,3),(3,4),(5,6),(6,45)]

# enumerate를 활용하는 방식을 아래와 같이 설명
a: list = ['a1', 'a2', 'a3']

for i in range(len(a)):
    print(i, a[i], end=' ')
print()
i: int = 0
for v in a:
    print(i, v, end=' ')
    i += 1
print()
for i, v in enumerate(a):
    print(i, v, end=' ')

# 나눗셈 연산자
print(5 / 3)  # 1.6666666666666666667
print(type(5 / 3))  # <class 'float'>
print(5 // 3)  # 1
print(int(5 / 3))  # 1
print(type(int(5 / 3)))  # <class 'int'>
print(5 % 3)  # 2
print(divmod(5, 3))  # (1, 2) -> 몫과 나머지를 한꺼번에 구할 수 있다.

# print
print('A1', 'B2')  # A1 B2 (한글자 공백으로 띄어서)
print('A1', 'B2', sep=',')  # A1,B2 (구분자를 추가한다.)
print('aa', end=' ')
print('bb')  # aa bb(윗줄 합쳐서)

# idx와 fruit가 정의되어 있다고 할때 idx에 1을 더해서 fruit와 함께 출력하는 방법은?
idx: int = 1
fruit: str = 'Apple'
print('{0}: {1}'.format(idx + 1, fruit))  # 2: Apple
print('{}: {}'.format(idx + 1, fruit))  # 2: Apple

# formated string literal 변수를 뒤에 별도로 부여할 필요 없이 마치 템플릿을 사용하듯 인라인으로 삽입하여 편리하게 사용할 수 있게 해주는 것
print(f'{idx + 1}: {fruit}')  # 2: Apple 파이썬 3.6이상부터 지원한다.


# pass
class MyClass(object):
    def method_a(self):
        pass

    def method_b(self):
        pass

# pass는 널 연산으로 아무것도 하지 않는 기능이다. 아무 역할을 하지 않는 pass를 지정하면 인덴트 오류 같은 불필요한 오류를 방지할 수 있다.
