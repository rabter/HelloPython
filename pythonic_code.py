"""
    파이썬스러운 코드에 대한 내용입니다.
    인덱스, 슬라이스
"""
MY_NUMBERS = (4, 5, 3, 9)

#print(MY_NUMBERS[-1])
#print(MY_NUMBERS[::])
#print(MY_NUMBERS[0:3:2])

INTERVAL = slice(1, 7, 2)
print(MY_NUMBERS[INTERVAL])
