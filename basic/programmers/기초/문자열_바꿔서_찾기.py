"""
문제: 문자열 바꿔서 찾기

myString의 'A'와 'B'를 서로 바꾼 문자열에 pat이 포함되면 1을,
포함되지 않으면 0을 반환한다.
"""


# 내가 이해하기 쉬운 풀이: 문자를 하나씩 확인하며 서로 바꾼다.
def my_solution(myString, pat):
    changed = ""

    for char in myString:
        if char == "A":
            changed += "B"
        else:
            changed += "A"

    return int(pat in changed)


# 참고 풀이: translate()로 두 문자를 동시에 바꾼다.
def best_solution(myString, pat):
    changed = myString.translate(str.maketrans({"A": "B", "B": "A"}))
    return int(pat in changed)


if __name__ == "__main__":
    print(my_solution("ABBAA", "AABB"))
    print(best_solution("ABBAA", "AABB"))
