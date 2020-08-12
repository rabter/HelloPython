"""
    first class function에 관련된 예제 입니다.
    변수나 데이터 구조 안에 할당 가능
    함수 인수 전달 가능
    함수 결과로 반환 가능
    위 세가지 조건이 충족되면 first class function
    파이썬의 모든 것은 객체이며 파이썬은 일급 객체 언어이다
"""
def square(num: int) -> int:
    """
        인자로 받은 수를 두 번 곱하는 함수 입니다.
    """
    return num * num


def my_map(func, arg_list):
    """
        first class function
    """
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

NUM_LIST = [1, 2, 3, 4, 5]

SQUARES = my_map(square, NUM_LIST)

print(SQUARES)

def hello_world(num):
    """
        객체할당 예제
    """
    for _ in range(num):
        print("Hello World")

GREET = hello_world
GREET(3)
