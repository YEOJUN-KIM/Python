"""
문제: 정수를 나선형으로 배치하기

n × n 배열에 1부터 n²까지 오른쪽 → 아래 → 왼쪽 → 위 순서로
방향을 바꾸며 시계 방향의 나선형으로 채운다.
"""


# 원래 풀이: 내 if/elif 구조를 유지하고 오류를 수정한 코드
def my_solution(n):
    arr = []
    for a in range(n):
        arr.append([])
        for b in range(n):
            arr[a].append(0)

    mode = 'd'
    i = 0
    j = 0

    for k in range(n ** 2):
        arr[i][j] = k + 1

        if k == n ** 2 - 1:
            break

        if mode == 'd':
            if j + 1 < n and arr[i][j + 1] == 0:
                j += 1
            else:
                mode = 's'
                i += 1

        elif mode == 's':
            if i + 1 < n and arr[i + 1][j] == 0:
                i += 1
            else:
                mode = 'a'
                j -= 1

        elif mode == 'a':
            if j - 1 >= 0 and arr[i][j - 1] == 0:
                j -= 1
            else:
                mode = 'w'
                i -= 1

        elif mode == 'w':
            if i - 1 >= 0 and arr[i - 1][j] == 0:
                i -= 1
            else:
                mode = 'd'
                j += 1

    return arr


# 모범 답안: 방향별 이동량을 딕셔너리로 관리
def best_solution(n):
    arr = []
    for a in range(n):
        arr.append([])
        for b in range(n):
            arr[a].append(0)

    # 방향별 (행 변화량, 열 변화량)
    directions = {
        'd': (0, 1),   # 오른쪽
        's': (1, 0),   # 아래
        'a': (0, -1),  # 왼쪽
        'w': (-1, 0)   # 위
    }
    next_mode = {'d': 's', 's': 'a', 'a': 'w', 'w': 'd'}

    mode = 'd'
    i = 0
    j = 0

    for k in range(n ** 2):
        arr[i][j] = k + 1

        if k == n ** 2 - 1:
            break  # 마지막 숫자를 넣었으면 이동하지 않음

        di, dj = directions[mode]
        ni = i + di
        nj = j + dj

        # 다음 위치가 배열 안에 있고 빈칸인지 확인
        if not (0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0):
            mode = next_mode[mode]
            di, dj = directions[mode]
            ni = i + di
            nj = j + dj

        i = ni
        j = nj

    return arr


if __name__ == "__main__":
    print(my_solution(3))
    print(best_solution(3))
