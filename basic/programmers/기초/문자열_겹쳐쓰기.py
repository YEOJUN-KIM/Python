"""
문제: 문자열 겹쳐쓰기

my_string의 인덱스 s부터 overwrite_string의 길이만큼을
overwrite_string으로 바꾼 문자열을 반환한다.
"""


# 내가 이해하기 쉬운 풀이: 리스트로 바꾼 뒤 각 위치의 문자를 수정한다.
def my_solution(my_string, overwrite_string, s):
    characters = list(my_string)

    for i in range(len(overwrite_string)):
        characters[s + i] = overwrite_string[i]

    return "".join(characters)


# 참고 풀이: 문자열은 직접 수정할 수 없으므로 앞, 새 문자열, 뒤를 연결한다.
def best_solution(my_string, overwrite_string, s):
    end = s + len(overwrite_string)
    return my_string[:s] + overwrite_string + my_string[end:]


if __name__ == "__main__":
    print(my_solution("He11oWor1d", "lloWorl", 2))
    print(best_solution("He11oWor1d", "lloWorl", 2))
