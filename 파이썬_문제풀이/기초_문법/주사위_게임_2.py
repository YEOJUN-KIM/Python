"""
문제: 주사위 게임 2

세 주사위의 숫자가 모두 다르면 일차식의 합을, 두 숫자만 같으면
일차식과 이차식의 곱을, 모두 같으면 일차식부터 삼차식까지의 곱을 반환한다.
"""


# 내가 작성한 풀이 (`a != b != c` 조건을 수정)
def my_solution(a, b, c):
    if a == b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or a == c or b == c:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


# 모범 답안: set으로 서로 다른 숫자의 개수를 확인
def best_solution(a, b, c):
    check = len(set([a, b, c]))

    if check == 1:
        return 3 * a * 3 * (a**2) * 3 * (a**3)
    elif check == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


if __name__ == "__main__":
    print(my_solution(2, 6, 1))
    print(best_solution(2, 6, 1))
