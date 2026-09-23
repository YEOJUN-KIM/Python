"""
문제: 세 개의 구분자

a, b, c를 구분자로 문자열을 나누고 빈 문자열은 제외한다.
결과가 비어 있으면 ["EMPTY"]를 반환한다.
내 풀이는 올바른 풀이이며, 다른 방법을 비교하기 위해 함께 기록한다.
"""

import re


# 내 풀이: 문자를 하나씩 확인하며 구분자 사이의 문자열을 모은다.
def my_solution(myStr):
    answer = []
    value = ''
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c':
            if value != '':
                answer.append(value)
                value = ''
        else:
            value += myStr[i]

    if value != '':
        answer.append(value)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer


# 참고 답안 1: 정규표현식의 |는 '또는', if m은 빈 문자열 제외를 뜻한다.
def regex_solution(myStr):
    answer = [m for m in re.split('a|b|c', myStr) if m]
    if len(answer) == 0:
        answer = ["EMPTY"]
    return answer


# 참고 답안 2: 구분자를 a로 통일한 뒤 split()으로 나눈다.
def replace_solution(myStr):
    s = myStr.replace('b', 'a')
    s = s.replace('c', 'a')
    s = s.split('a')
    answer = []
    for x in s:
        if x:
            answer.append(x)
    if not answer:
        return ["EMPTY"]
    return answer


if __name__ == "__main__":
    text = "baconlettucetomato"
    print(my_solution(text))
    print(regex_solution(text))
    print(replace_solution(text))
