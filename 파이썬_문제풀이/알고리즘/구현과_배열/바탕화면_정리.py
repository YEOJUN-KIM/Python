"""
문제: 바탕화면 정리

바탕화면에서 파일("#")이 있는 모든 칸을 포함하는
가장 작은 드래그 영역 [시작 행, 시작 열, 끝 행, 끝 열]을 구한다.
"""


def solution(wallpaper):
    answer = [51, 51, 0, 0]

    for i, values in enumerate(wallpaper):
        # 문자열도 반복 가능하므로 enumerate()로 인덱스와 문자를 얻을 수 있다.
        for j, value in enumerate(values):
            if value == '#':
                answer[0] = min(answer[0], i)
                answer[1] = min(answer[1], j)

                # 우측 아래는 마지막 파일 칸의 인덱스가 아니라
                # 그 칸 전체를 포함하는 끝 경계이므로 1을 더한다.
                answer[2] = max(answer[2], i + 1)
                answer[3] = max(answer[3], j + 1)

    return answer


if __name__ == "__main__":
    sample = [".#...", "..#..", "...#."]
    print(solution(sample))  # [0, 1, 3, 4]
