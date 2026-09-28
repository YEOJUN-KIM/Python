"""
문제: 문자열의 뒤의 n글자

문자열 my_string의 뒤에서부터 n글자로 이루어진 문자열을 반환한다.
"""


# 내가 작성한 풀이
def my_solution(my_string, n):
    answer = ""

    for i in range(n, 0, -1):
        answer += my_string[-i]

    return answer


# 참고 풀이: 음수 인덱스와 슬라이싱으로 뒤의 n글자를 가져온다.
def best_solution(my_string, n):
    return my_string[-n:]


if __name__ == "__main__":
    text = "ProgrammerS123"
    print(my_solution(text, 3))
    print(best_solution(text, 3))
