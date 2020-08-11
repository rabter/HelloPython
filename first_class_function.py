"""
    first class function에 관련된 예제 입니다.
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
