"""
문제: 원소들의 곱과 합

모든 원소의 곱이 모든 원소의 합의 제곱보다 작으면 1을,
그렇지 않으면 0을 반환한다.
"""


# 내가 작성한 풀이
def my_solution(num_list):
    product = 1
    total = 0

    for number in num_list:
        product *= number
        total += number

    squared_sum = total * total

    if product < squared_sum:
        return 1

    return 0


# 참고 풀이: 비교 결과인 True 또는 False를 int로 변환한다.
def best_solution(num_list):
    product = 1

    for number in num_list:
        product *= number

    return int(product < sum(num_list) ** 2)


if __name__ == "__main__":
    numbers = [3, 4, 5, 2, 1]
    print(my_solution(numbers))
    print(best_solution(numbers))

