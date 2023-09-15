# 문자 (char) >>> 코드 숫자와 1:1 매칭
if 'A' == 97:
    print('같음!')
else:
    print('다름!')

# 문자열 (string)
# itoa(), atoi()
# 파이썬에서는 chr(), ord() 내장함수가 있음
# print(ord('A'))
# print(chr(65))

def itoa(i):  # 숫자를 문자열로 만듬 123 > '123'
    # 숫자 한자리 한자리를 떼어서 문자열로 만든 다음 붙이기
    # 123 나누기 10을 반복적으로 하면 3 > 2 > 1 순서로 떼어짐
    result = ''
    while True:
        if i == 0:
            break
        result = chr(i % 10 + ord('0')) + result
        # 얘는 숫자를 출력한 것 > 문자로 바꿔주기
        # chr() 함수를 이용하면 숫자형태 문자열 얻음
        i //= 10
    return result

print(itoa(123)


## 안돌아가 몰라 머리도 안돌아가 졸려
def atoi(n): # 문자열을 숫자로 만듬 '123' > 123
    result = 0
    # 문자열 한자리씩 읽어와서 숫자로 바꾸어주고
    N = len(n)
    for i in range(N):
        # data[i] >> 숫자바꾸기
        tmp = ord(n[i]) - ord('0')
        result = result*10 + tmp
    return result

result = atoi('67123')
print(f'{result} : {type(result)}')
    # 기존 숫자에 * 10 + 바꾼 숫자
    # 모든 자리수에 대해서 반복