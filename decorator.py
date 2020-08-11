"""
    데코레이터 예제
    decorator = syntax sugar
"""

#from dataclasses import dataclass

def original(name):
    """
        이름을 출력
    """
    print("I'm " + name)

def modifier(original_function):
    """
        데코레이터를 위한 함수
    """
    def wrapper_function(*args, **kwargs):
        print('{} 함수가 호출되기 전 입니다.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@modifier
def changed(name):
    """
        수정된 함수
    """
    print("I'm " + name + " using modifier decorator")

print(changed("Charles Hong"))
