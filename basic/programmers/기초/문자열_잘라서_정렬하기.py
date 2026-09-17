"""
문제: 문자열 잘라서 정렬하기

myString을 'x'를 기준으로 나눈 뒤, 빈 문자열을 제외하고
사전순으로 정렬한 리스트를 반환한다.
"""


# 내가 이해하기 쉬운 풀이: 필요한 값만 새로운 리스트에 추가한다.
def my_solution(myString):
    answer = []

    for value in myString.split("x"):
        if value != "":
            answer.append(value)

    answer.sort()
    return answer


# 참고 풀이: 리스트 컴프리헨션으로 빈 문자열을 제외한 뒤 정렬한다.
def best_solution(myString):
    return sorted([value for value in myString.split("x") if value != ""])


if __name__ == "__main__":
    text = "axbxcxxdx"
    print(my_solution(text))
    print(best_solution(text))
