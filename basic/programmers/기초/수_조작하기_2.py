"""
문제: 수 조작하기 2

연속된 두 수의 차이를 이용해 숫자를 조작한 명령을 문자열로 반환한다.
"""


# 내가 작성한 풀이 (변수 이름과 불필요한 초기화를 정리)
def my_solution(numLog):
    answer = ""
    previous = numLog[0]
    command = dict(zip([1, -1, 10, -10], ["w", "s", "d", "a"]))

    for current in numLog[1:]:
        difference = current - previous
        answer += command[difference]
        previous = current

    return answer


# 참고 풀이: zip으로 이전 값과 현재 값을 함께 순회
def best_solution(numLog):
    answer = ""
    command = {1: "w", -1: "s", 10: "d", -10: "a"}

    for previous, current in zip(numLog, numLog[1:]):
        answer += command[current - previous]

    return answer


if __name__ == "__main__":
    sample = [0, 1, 0, 10, 0]
    print(my_solution(sample))
    print(best_solution(sample))
