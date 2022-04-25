import pprint

pprint.pprint(locals())
# 로컬에 선언된 모든 변수들의 조회가 가능하다.
# 함수 내부에서는 내부의 로컬 정보를 조회해 잘못 선언한 부분이 없는지 확인하는 용도로 사용할 수 있다.


# 함수는 camelCase로 작성하고 변수는 모두 snake_case로 작성한다.

# 리스트 컴프레헨션이 복잡할 시에는 줄을 나누어주면 편하다.
# 리스트 컴프레헨션이 2줄이 넘어간다 싶을 때에는 그냥 for문을 써주는 것이 더 보기 좋다.

# 구글에서 정한 파이썬 스타일 가이드 중요한점 -> 아래와 같이 argument에 기본값으로 []나 {}을 사용하는 것은 지양한다.
# ex)
def foo(a, b=[]):
    pass

def foo(a, b: dict = {}):
    pass 
# 위처럼 하면 안된다.
# 대신에 불변객체(Immutable Object)를 사용한다. None을 명시적으로 할당하는 것도 좋은 방법이다.
def foo(a,b=None):
    if b is None:
        b = []

def foo(a,b:Optional[Sequence]=None):
    if b is None:
        b = []
# 위의 예제들은 좋은 예이다.


# True False를 판별할 때는 암시적(implicit)인 방법으로 사용하는 것이 간결하고 가독성이 높다.
# Good
if not users:
    print("no users")

if foo == 0:
    self.handle_zero()

if i % 10 == 0:
    self.handle_multiple_of_ten()

# Bad
if len(users) == 0: # 길이가 없다는 말이고 이 경우에 not으로 충분하다
    print('no users') 

if foo is not None and not foo: # 정수를 처리할 때는 암시적으로 거짓 여부를 판별하기 보다는 비교대상이 되는 정수값을 직접 비교해야한다.
    self.handle_zero()

if not i % 10: # 연산 결과가 0인것을 정수로 처리하지 않고 암시적 거짓여부로 판별하는 것은 위험하다. 뿐만 아니라 가독성이 떨어진다.
    self.handle_multiple_of_ten()

# 한줄당 최대 길이는 80자로 제한한다.
