"""프로그래머스: 올바른 괄호"""


def solution(s):
    """괄호가 한 종류이므로 열린 괄호의 개수만 저장한다."""
    count = 0

    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0


def solution_with_stack(s):
    """append()와 pop()을 사용하는 일반적인 스택 풀이."""
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    test_cases = ["()()", "(())()", ")()(", "(()(", "())(()"]

    for test in test_cases:
        print(test, solution(test), solution_with_stack(test))
