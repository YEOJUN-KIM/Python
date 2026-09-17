"""
문제: n개 간격의 원소들

num_list의 첫 번째 원소부터 n개 간격으로 저장된 원소들을 반환한다.
"""


# 내가 작성한 방식: range()의 세 번째 값으로 간격을 지정한다.
def my_solution(num_list, n):
    answer = []

    for i in range(0, len(num_list), n):
        answer.append(num_list[i])

    return answer


# 참고 풀이: 슬라이싱의 세 번째 값으로 간격을 지정한다.
def best_solution(num_list, n):
    return num_list[::n]


if __name__ == "__main__":
    numbers = [4, 2, 6, 1, 7, 6]
    print(my_solution(numbers, 2))
    print(best_solution(numbers, 2))
