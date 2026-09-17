"""
문제: 글자 이어 붙여 문자열 만들기

index_list의 순서대로 my_string의 문자를 이어 붙인 문자열을 반환한다.
"""


# 내가 작성한 풀이
def my_solution(my_string, index_list):
    answer = ""

    for i in range(len(index_list)):
        answer += my_string[index_list[i]]

    return answer


# 참고 풀이: 인덱스에 해당하는 문자를 꺼내 join()으로 연결한다.
def best_solution(my_string, index_list):
    return "".join(my_string[idx] for idx in index_list)


if __name__ == "__main__":
    text = "cvsgiorszzzmrpaqpe"
    indexes = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
    print(my_solution(text, indexes))
    print(best_solution(text, indexes))
