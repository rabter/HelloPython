"""
    파이썬 코드 포매팅 관련 내용입니다.
    Type Hinting
"""

def docstring():
    """
        docsting은 파이썬 소스 코드에 포함된 문서(documentation)입니다.
        주석(comment)와는 차이가 있습니다.
        최대한 코드에 주석을 피하고 docstring으로 문서화 하는 것이 바람직합니다.
    """


def annotation(width: int, height: int) -> int:
    """
        width와 height 값을 곱한 결과를 return 하는 함수입니다.
    """
    return width*height

print(annotation(10, 10))
