"""
문제: rny_string

문자열 rny_string의 모든 'm'을 'rn'으로 바꾼 문자열을 반환한다.
"""


# 내가 작성한 풀이
def my_solution(rny_string):
    answer = ""

    for char in rny_string:
        if char == "m":
            answer += "rn"
        else:
            answer += char

    return answer


# 참고 풀이: replace()로 문자열의 모든 'm'을 'rn'으로 바꾼다.
def best_solution(rny_string):
    return rny_string.replace("m", "rn")


if __name__ == "__main__":
    text = "masterpiece"
    print(my_solution(text))
    print(best_solution(text))
