"""
문제: 홀짝에 따른 다른 값

양의 정수 n이 홀수라면 n 이하의 모든 홀수의 합을 반환하고,
n이 짝수라면 n 이하의 모든 짝수의 제곱의 합을 반환한다.
"""


# 내가 작성한 풀이
def my_solution(n):
    answer = 0

    if n % 2 == 1:
        for number in range(n + 1):
            if number % 2 == 1:
                answer += number
    else:
        for number in range(n + 1):
            if number % 2 == 0:
                answer += number * number

    return answer


# 참고 풀이
def best_solution(n):
    if n % 2:
        return sum(range(1, n + 1, 2))

    return sum(number * number for number in range(2, n + 1, 2))


if __name__ == "__main__":
    print(my_solution(7))
    print(best_solution(7))

