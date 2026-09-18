"""
문제: 가까운 1 찾기

정수 배열 arr에서 인덱스 idx보다 크거나 같은 위치에 있는
첫 번째 1의 인덱스를 반환하고, 없다면 -1을 반환한다.
"""


# 내가 작성한 풀이
def my_solution(arr, idx):
    for pos, value in enumerate(arr[idx:], start=idx):
        if value == 1:
            return pos

    return -1


# 모범 답안
def best_solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i

    return -1


if __name__ == "__main__":
    sample = [0, 0, 1, 0, 1]
    print(my_solution(sample, 1))
    print(best_solution(sample, 1))
