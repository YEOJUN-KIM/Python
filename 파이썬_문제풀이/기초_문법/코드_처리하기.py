"""
문제: 코드 처리하기

문자열 code를 앞에서부터 읽으면서 문자 "1"을 만나면 mode를 바꾼다.
mode가 0이면 짝수 인덱스의 문자를, mode가 1이면 홀수 인덱스의
문자를 ret에 추가한다. 결과가 빈 문자열이면 "EMPTY"를 반환한다.
"""


# 내가 작성한 풀이 (`not mode`를 재대입하도록 수정)
def my_solution(code):
    mode = False
    ret = ""

    for idx in range(len(code)):
        if code[idx] == "1":
            mode = not mode
        else:
            if mode is True and idx % 2 == 1:
                ret += code[idx]
            if mode is False and idx % 2 == 0:
                ret += code[idx]

    if ret == "":
        ret = "EMPTY"

    return ret


# 모범 답안
def best_solution(code):
    answer = ""
    mode = 0

    for i in range(len(code)):
        if code[i] == "1":
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else "EMPTY"


if __name__ == "__main__":
    print(my_solution("abc1abc1abc"))
    print(best_solution("abc1abc1abc"))
