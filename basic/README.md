# Python 기초 학습 노트

프로그래머스 문제를 풀면서 알게 된 문법과 자주 하는 실수를 짧게 정리한다.

## 반복문

### 기본 순회

- `for value in arr:` — 값을 하나씩 순회
- `for i in range(len(arr)):` — 인덱스로 순회
- `for value in numbers:` — 정수 리스트의 값을 직접 꺼내 `total += value`, `product *= value`처럼 누적 계산에 활용

### `range()`로 범위 정하기

- `range(start, end, step)` — `start`부터 `end` 직전까지 `step` 간격으로 순회하며, `step`을 생략하면 `1` (`range()`는 쉼표 사용)
- `range(start, end, -1)` — 숫자를 1씩 줄이며 역순으로 순회

### `enumerate()`로 인덱스와 값 함께 순회하기

`enumerate(arr)`는 리스트의 인덱스와 값을 한 번에 꺼낸다.

```python
arr = ["a", "b", "c"]

for i, value in enumerate(arr):
    print(i, value)
```

반복할 때 `i`에는 `0, 1, 2`가, `value`에는 `"a", "b", "c"`가 차례로 들어간다. 다음 코드와 같은 동작이다.

```python
for i in range(len(arr)):
    value = arr[i]
    print(i, value)
```

값만 필요하면 `for value in arr`, 인덱스와 값이 모두 필요하면 `enumerate()`를 사용한다.

## 리스트 컴프리헨션

반복문으로 새로운 리스트를 만드는 코드를 한 줄로 줄이는 문법이다.

```python
# 일반 for문
answer = []
for value in arr:
    answer.append(value * 2)

# 리스트 컴프리헨션
answer = [value * 2 for value in arr]
```

기본 구조는 `[리스트에 넣을 값 for 변수 in 반복할 자료]`이며, 뒤에 `if`를 붙이면 조건에 맞는 값만 넣는다.

```python
# 빈 문자열이 아닌 값만 넣기
answer = [value for value in arr if value != ""]
```

`for value in arr`로 값을 하나씩 꺼내고, 앞의 표현식 결과를 새 리스트에 넣는 순서로 이해한다.

## 연산자

- `a ** b` — a의 b제곱 (`2 ** 3`은 `8`)

## 문자열

### 순회와 확인

- `for char in text:` — 문자를 한 글자씩 순회
- `"python" in text` / `"python" not in text` — 문자열 포함 / 미포함 확인

### 인덱스와 슬라이싱

- `text[-1]` — 마지막 문자 가져오기
- `text[:n]` / `text[-n:]` — 앞에서 / 뒤에서 n글자 가져오기
- `text[start:end:step]` — `step` 간격으로 슬라이싱 (슬라이싱은 콜론 사용)

> 관련 문제: [`문자열의 뒤의 n글자`](./programmers/기초/문자열의_뒤의_n글자.py)

### 문자열 변경

- `text.upper()` / `text.lower()` — 대문자 / 소문자로 변경
- `text.swapcase()` — 대문자는 소문자로, 소문자는 대문자로 서로 변경
- `text.replace("바꿀 값", "새 값")` — 일치하는 값을 모두 변경
- `text.translate(str.maketrans({"A": "B", "B": "A"}))` — `A`와 `B`처럼 여러 문자를 동시에 교체

> **주의:** 문자열은 원본이 직접 바뀌지 않으므로 결과를 변수에 저장하거나 바로 반환한다. 두 문자를 서로 바꿀 때는 연속 `replace()` 대신 `translate()`를 사용한다.

> 관련 문제: [`rny_string`](./programmers/기초/rny_string.py), [`문자열 바꿔서 찾기`](./programmers/기초/문자열_바꿔서_찾기.py)

### 나누기와 연결하기

- `text.split()` — 공백을 기준으로 나눠 리스트로 반환
- `text.split(",")` — 쉼표를 기준으로 나눠 리스트로 반환
- `"".join(words)` / `"-".join(words)` — 문자열들을 붙이기 / `-`로 연결하기

### 공백과 특수문자

- `text.strip()` / `text.lstrip()` / `text.rstrip()` — 양쪽 / 왼쪽 / 오른쪽 끝 공백 제거
- `text.replace(" ", "")` — 문자열의 모든 일반 공백 제거
- `\\` / `\"` — 문자열 안에서 역슬래시(`\`) / 큰따옴표(`"`) 출력

### 인덱스에 해당하는 문자 조합하기

```python
# 일반 for문
answer = ""
for idx in index_list:
    answer += my_string[idx]

# 리스트 컴프리헨션과 join()
answer = "".join(my_string[idx] for idx in index_list)
```

> 관련 문제: [`글자 이어 붙여 문자열 만들기`](./programmers/기초/글자_이어_붙여_문자열_만들기.py)

## 리스트

- `arr.append(value)` — 리스트 마지막에 값 추가

## 딕셔너리

- `data[key]` — 키에 해당하는 값 가져오기
- `dict(zip(keys, values))` — 키 목록과 값 목록을 묶어 딕셔너리 생성

```python
key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
```

## 내장 함수

- `sum(numbers)` — 숫자들의 합계
- `import math` 후 `math.prod(numbers)` — 숫자들을 모두 곱한 값
- `sum(numbers) / len(numbers)` — 숫자들의 평균 (`avg()` 기본 함수는 없음)
- `max(a, b)` / `min(a, b)` — 큰 값 / 작은 값
- `zip(a, b)` — 두 자료에서 같은 위치의 값끼리 묶기
- `list(map(int, input().split()))` — 공백으로 구분해 입력받은 값들을 정수 리스트로 변환

## 여러 기능 조합

```python
def solution(n, control):
    key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum(key[char] for char in control)
```

## 실수 기록

### `range()`에서 콜론 사용

`range(start, end, step)`은 값을 쉼표로 구분하며, `end`는 범위에 포함하지 않는다.

> 관련 문제: [`n개 간격의 원소들`](./programmers/기초/n개_간격의_원소들.py)

### 빈 리스트의 존재하지 않는 위치에 대입

빈 리스트에는 아직 `0`번 위치가 없으므로 새 값은 `append()`로 추가한다.

```python
answer[i] = value     # 이미 존재하는 위치 변경
answer.append(value)  # 리스트 끝에 새 값 추가
```

### `print()`가 값 사이에 넣는 공백

`print(a, b)`는 값 사이에 공백을 넣는다. 붙여 출력하려면 `print(a, b, sep="")`를 사용한다.

### 문자열의 특정 인덱스에 대입

문자열은 특정 인덱스를 직접 수정할 수 없다. `text[i] = value`는 `TypeError`가 발생하므로 슬라이싱으로 새 문자열을 만든다.

```python
# 잘못된 방법
my_string[s] = overwrite_string[0]

# 문자열 일부 덮어쓰기
end = s + len(overwrite_string)
my_string = my_string[:s] + overwrite_string + my_string[end:]
```

> 관련 문제: [`문자열 겹쳐쓰기`](./programmers/기초/문자열_겹쳐쓰기.py)

### 순회 중인 리스트에서 원소 삭제

`for`문으로 리스트를 순회하면서 `remove()`하면 원소가 이동해 일부를 건너뛸 수 있다. 필요한 값만 새 리스트에 추가한다.

> 관련 문제: [`문자열 잘라서 정렬하기`](./programmers/기초/문자열_잘라서_정렬하기.py)

## 문제 풀이 기록 기준

- 새롭게 알게 된 문법이나 함수가 있는 문제
- 틀렸거나 오래 고민한 문제
- 더 간단하거나 배울 점이 있는 풀이가 나온 문제
- 나중에 다시 풀어 보고 싶은 문제

쉽게 풀었고 새로운 내용이 없는 문제는 코드만 남기거나 넘어간다.
