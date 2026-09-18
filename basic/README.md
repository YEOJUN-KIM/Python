# Python 기초 학습 노트

프로그래머스 문제를 풀면서 알게 된 문법과 자주 하는 실수를 짧게 정리한다.

<br>

---

## 🟦 01 · 반복문

### 🔹 기본 순회

| 문법 | 용도 |
| --- | --- |
| `for value in arr:` | 값을 하나씩 순회 |
| `for i in range(len(arr)):` | 인덱스로 순회 |
| `for value in numbers:` | 정수 리스트의 값을 직접 꺼내 `total += value`, `product *= value`처럼 누적 계산에 활용 |

### 🔹 `range()`로 범위 정하기

| 문법 | 용도 |
| --- | --- |
| `range(start, end, step)` | `start`부터 `end` 직전까지 `step` 간격으로 순회하며, `step`을 생략하면 `1` (`range()`는 쉼표 사용) |
| `range(start, end, -1)` | 숫자를 1씩 줄이며 역순으로 순회 |

### 🔹 `enumerate()`로 인덱스와 값 함께 순회하기

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

### 🔹 반복문에서 언패킹하기

각 원소의 값 개수를 알고 있다면 여러 변수로 바로 나눠 받을 수 있다. 값과 변수의 개수는 같아야 한다.

```python
queries = [[0, 3], [1, 2]]

for i, j in queries:
    print(i, j)
```

다음 코드와 같은 의미다.

```python
for query in queries:
    i = query[0]
    j = query[1]
```

<br>

---

## 🟦 02 · 리스트 컴프리헨션

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

<br>

---

## 🟦 03 · 연산자

- `a ** b` — a의 b제곱 (`2 ** 3`은 `8`)

<br>

---

## 🟦 04 · 문자열

### 🔹 순회와 확인

| 문법 | 용도 |
| --- | --- |
| `for char in text:` | 문자를 한 글자씩 순회 |
| `"python" in text` / `"python" not in text` | 문자열 포함 / 미포함 확인 |

### 🔹 인덱스와 슬라이싱

| 문법 | 용도 |
| --- | --- |
| `text[-1]` | 마지막 문자 가져오기 |
| `text[:n]` / `text[-n:]` | 앞에서 / 뒤에서 n글자 가져오기 |
| `text[start:end:step]` | `step` 간격으로 슬라이싱 (슬라이싱은 콜론 사용) |
| `text[::-1]` | 문자열 전체를 역순으로 뒤집기 |

```python
text[s:e + 1][::-1]  # 인덱스 s부터 e까지 뒤집기
```

> 관련 문제: [`문자열의 뒤의 n글자`](./programmers/기초/문자열의_뒤의_n글자.py)

### 🔹 문자열 변경

| 문법 | 용도 |
| --- | --- |
| `text.upper()` / `text.lower()` | 대문자 / 소문자로 변경 |
| `text.swapcase()` | 대문자는 소문자로, 소문자는 대문자로 서로 변경 |
| `text.replace("바꿀 값", "새 값")` | 일치하는 값을 모두 변경 |
| `text.translate(str.maketrans({"A": "B", "B": "A"}))` | `A`와 `B`처럼 여러 문자를 동시에 교체 |

> **주의:** 문자열은 원본이 직접 바뀌지 않으므로 결과를 변수에 저장하거나 바로 반환한다. 두 문자를 서로 바꿀 때는 연속 `replace()` 대신 `translate()`를 사용한다.

> 관련 문제: [`rny_string`](./programmers/기초/rny_string.py), [`문자열 바꿔서 찾기`](./programmers/기초/문자열_바꿔서_찾기.py)

### 🔹 나누기와 연결하기

| 문법 | 용도 |
| --- | --- |
| `text.split()` | 공백을 기준으로 나눠 리스트로 반환 |
| `text.split(",")` | 쉼표를 기준으로 나눠 리스트로 반환 |
| `"".join(words)` / `"-".join(words)` | 문자열들을 붙이기 / `-`로 연결하기 |

### 🔹 공백과 특수문자

| 문법 | 용도 |
| --- | --- |
| `text.strip()` / `text.lstrip()` / `text.rstrip()` | 양쪽 / 왼쪽 / 오른쪽 끝 공백 제거 |
| `text.replace(" ", "")` | 문자열의 모든 일반 공백 제거 |
| `\\` / `\"` | 문자열 안에서 역슬래시(`\`) / 큰따옴표(`"`) 출력 |

<br>

---

## 🟦 05 · 리스트

- `arr.append(value)` — 리스트 마지막에 값 추가
- `if not answer:` — 리스트가 비어 있을 때 실행

| 문법 | 용도 |
| --- | --- |
| `stk.append(value)` | 마지막에 값을 추가 (`push` 역할) |
| `stk.pop()` | 마지막 값을 꺼내면서 삭제 |
| `stk.pop(i)` | `i`번 값을 꺼내면서 삭제 |
| `stk.remove(value)` | 처음 발견되는 `value`를 삭제 |

### 🔹 리스트의 두 값 교환하기

파이썬에서는 임시 변수 없이 두 위치의 값을 바로 교환할 수 있다.

```python
answer[i], answer[j] = answer[j], answer[i]
```

다음 코드와 같은 의미다.

```python
temp = answer[i]
answer[i] = answer[j]
answer[j] = temp
```

### 🔹 `set`으로 중복 제거하기

`set()`은 중복을 제거한다. 따라서 `len(set([a, b, c]))`로 서로 다른 숫자의 개수를 알 수 있다.

```python
len(set([2, 2, 5]))  # 2
```

<br>

---

## 🟦 06 · 딕셔너리

| 문법 | 용도 |
| --- | --- |
| `data[key]` | 키에 해당하는 값 가져오기 |
| `dict(zip(keys, values))` | 키 목록과 값 목록을 묶어 딕셔너리 생성 |

```python
key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
```

<br>

---

## 🟦 07 · 내장 함수

| 문법 | 용도 |
| --- | --- |
| `sum(numbers)` | 숫자들의 합계 |
| `import math` 후 `math.prod(numbers)` | 숫자들을 모두 곱한 값 |
| `sum(numbers) / len(numbers)` | 숫자들의 평균 (`avg()` 기본 함수는 없음) |
| `max(a, b)` / `min(a, b)` | 큰 값 / 작은 값 |
| `zip(a, b)` | 두 자료에서 같은 위치의 값끼리 묶기 |
| `list(map(int, input().split()))` | 공백으로 구분해 입력받은 값들을 정수 리스트로 변환 |
| `any(조건들)` | 조건 중 하나라도 참이면 `True` |
| `all(조건들)` | 모든 조건이 참이면 `True` |

```python
if not any(char in text for char in "12346789"):
    print("금지된 문자가 하나도 없음")

if all(char in "05" for char in text):
    print("모든 문자가 0 또는 5")
```

<br>

---

## 🟦 08 · 여러 기능 조합

```python
def solution(n, control):
    key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum(key[char] for char in control)
```

<br>

---

## 🟥 09 · 실수 기록

### ❌ 01 · `range()`에서 콜론 사용

| 구분 | 내용 |
| --- | --- |
| 원인 | 슬라이싱의 콜론과 함수 인수의 쉼표를 혼동 |
| 해결 | `range(start, end, step)`처럼 쉼표 사용. 끝값 `end`는 제외 |
| 관련 문제 | [n개 간격의 원소들](./programmers/기초/n개_간격의_원소들.py) |

### ❌ 02 · 빈 리스트에 인덱스로 대입

| 구분 | 내용 |
| --- | --- |
| 원인 | `answer = []`에는 `0`번 위치도 없으므로 `answer[0] = value`는 오류 |
| 해결 | 새 원소는 `answer.append(value)`, 기존 위치 수정은 `answer[i] = value` |
| 관련 문제 | 별도 파일 없음 · 기본 문법 메모 |

### ❌ 03 · 출력 사이에 의도하지 않은 공백

| 구분 | 내용 |
| --- | --- |
| 원인 | `print(a, b)`는 기본적으로 두 값 사이에 공백을 넣음 |
| 해결 | `print(a, b, sep="")`로 붙여 출력 |
| 관련 문제 | 별도 파일 없음 · 기본 문법 메모 |

### ❌ 04 · 문자열 인덱스에 직접 대입

| 구분 | 내용 |
| --- | --- |
| 원인 | 문자열은 변경 불가능하므로 `text[i] = value`에서 `TypeError` 발생 |
| 해결 | 앞부분 + 덮어쓸 문자열 + 뒷부분으로 새 문자열 생성 |
| 관련 문제 | [문자열 겹쳐쓰기](./programmers/기초/문자열_겹쳐쓰기.py) |

```python
# 잘못된 방법
my_string[s] = overwrite_string[0]

# 해결
end = s + len(overwrite_string)
my_string = my_string[:s] + overwrite_string + my_string[end:]
```

### ❌ 05 · 순회 중인 리스트에서 삭제

| 구분 | 내용 |
| --- | --- |
| 원인 | `remove()`로 원소가 앞으로 이동하면 다음 원소를 건너뛸 수 있음 |
| 해결 | 필요한 값만 새 리스트에 추가 |
| 관련 문제 | [문자열 잘라서 정렬하기](./programmers/기초/문자열_잘라서_정렬하기.py) |

### ❌ 06 · `not`의 결과를 변수에 저장하지 않음

| 구분 | 내용 |
| --- | --- |
| 원인 | `not mode`는 반대 불리언 값을 계산할 뿐, 기존 `mode`를 바꾸지 않음 |
| 해결 | `mode = not mode`처럼 계산 결과를 다시 변수에 대입 |
| 관련 문제 | [코드 처리하기](./programmers/기초/코드_처리하기.py) |

```python
# 잘못된 방법: mode의 값은 바뀌지 않는다.
not mode

# 해결: 반대 값을 다시 저장한다.
mode = not mode
```

### ❌ 07 · 슬라이싱 대괄호 위치 혼동

| 구분 | 내용 |
| --- | --- |
| 원인 | `[names::5]`처럼 리스트 바깥에 대괄호를 작성함 |
| 해결 | 슬라이싱은 `자료[시작:끝:간격]` 형태이므로 `names[::5]`로 작성 |
| 관련 문제 | [5명씩](./programmers/기초/5명씩.py) |

```python
# 잘못된 방법
[names::5]

# 해결: names의 0, 5, 10, ...번 원소를 가져온다.
names[::5]
```

### ❌ 08 · 연속된 `!=`로 세 값 전체를 비교

| 구분 | 내용 |
| --- | --- |
| 원인 | `a != b != c`는 `a != b and b != c`라는 뜻이므로 `a`와 `c`는 비교하지 않음 |
| 해결 | `a != b and a != c and b != c`로 모두 비교하거나 `len({a, b, c}) == 3` 사용 |
| 관련 문제 | [주사위 게임 2](./programmers/기초/주사위_게임_2.py) |

```python
# a와 c가 같은 경우를 놓친다.
a != b != c

# 세 값이 모두 다른지 확인한다.
a != b and a != c and b != c
```

### ❌ 09 · 딕셔너리 사용 방법 미숙

| 구분 | 내용 |
| --- | --- |
| 원인 | 숫자와 딕셔너리 전체를 비교하려고 함 |
| 해결 | `dictionary[key]` 형태로 키에 해당하는 값을 가져옴 |
| 관련 문제 | [수 조작하기 2](./programmers/기초/수_조작하기_2.py) |

```python
command = {1: "w", -1: "s", 10: "d", -10: "a"}
command[10]  # "d"
```

### ❌ 10 · 리스트 삭제 메서드와 인덱싱 혼동

| 구분 | 내용 |
| --- | --- |
| 원인 | 마지막 원소를 삭제하려고 `stk.remove[-1]`을 사용함 |
| 해결 | 마지막 원소 삭제는 `stk.pop()`, 특정 값 삭제는 `stk.remove(value)` 사용 |
| 관련 문제 | 배열 만들기 4 |

```python
# 잘못된 방법
stk.remove[-1]

# 마지막 원소 삭제
stk.pop()
```

### ❌ 11 · 이차원 배열을 불필요하게 두 번 반복

| 구분 | 내용 |
| --- | --- |
| 원인 | `[s, e]` 안의 정수를 다시 `for i, j in value`로 언패킹하려 함 |
| 결과 | `TypeError: cannot unpack non-iterable int object` 발생 |
| 해결 | 각 내부 배열의 값이 2개라면 `for s, e in queries`로 바로 언패킹 |
| 관련 문제 | 문자열 여러 번 뒤집기 |

```python
# 잘못된 방법
for value in queries:
    for s, e in value:
        pass

# 해결
for s, e in queries:
    pass
```

### ❌ 12 · 값만 순회한 뒤 원래 위치를 구하려 함

| 구분 | 내용 |
| --- | --- |
| 원인 | `for value in arr[idx:]`는 원소의 값만 주므로 원래 인덱스를 바로 알 수 없음 |
| 해결 | `enumerate(arr[idx:], start=idx)` 또는 `range(idx, len(arr))` 사용 |
| 관련 문제 | [가까운 1 찾기](./programmers/기초/가까운_1_찾기.py) |

```python
for pos, value in enumerate(arr[idx:], start=idx):
    if value == 1:
        return pos
```

<br>

---

## 🟦 10 · 문제 풀이 기록 기준

- 새롭게 알게 된 문법이나 함수가 있는 문제
- 틀렸거나 오래 고민한 문제
- 더 간단하거나 배울 점이 있는 풀이가 나온 문제
- 나중에 다시 풀어 보고 싶은 문제

쉽게 풀었고 새로운 내용이 없는 문제는 코드만 남기거나 넘어간다.
