"""
문제: 5명씩

사람들의 이름이 담긴 리스트 names에서 앞에서부터 5명씩 묶었을 때,
각 그룹의 첫 번째 사람 이름을 반환한다.
"""


# 내가 작성한 풀이 (슬라이싱 문법을 수정)
def my_solution(names):
    answer = []

    for value in names[::5]:
        answer.append(value)

    return answer


# 모범 답안
def best_solution(names):
    return names[::5]


if __name__ == "__main__":
    sample = ["nami", "ahri", "jayce", "garen", "iv", "vex", "jinx"]
    print(my_solution(sample))
    print(best_solution(sample))
