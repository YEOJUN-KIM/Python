# Python 기초 학습 노트

프로그래머스 문제를 풀면서 새롭게 알게 된 문법과 자주 하는 실수를 기능별로 정리한다.

## 목차

- [조건문](#조건문)
- [반복문](#반복문)
- [문자열](#문자열)
- [리스트](#리스트)
- [딕셔너리](#딕셔너리)
- [내장 함수](#내장-함수)
- [실수 기록](#실수-기록)
- [문제 풀이 기록 기준](#문제-풀이-기록-기준)

---

## 조건문

### 홀수와 짝수 구분하기

> 학습일: 2026-09-17

나머지 연산자 `%`를 사용하면 홀수와 짝수를 구분할 수 있다.

```python
if k % 2 :
    print("짝수")
else:
    print("홀수")
```

정수는 홀수 또는 짝수이므로 짝수가 아닌 경우는 `else`로 처리할 수 있다.

---

## 반복문

### 값만 순회하기

> 학습일: 2026-09-17

리스트나 문자열에서 값만 필요할 때는 자료를 바로 순회한다.

```python
for value in arr:
    print(value)
```

### 인덱스로 순회하기

> 학습일: 2026-09-17

인덱스가 필요하면 `range(len(...))`를 사용할 수 있다.

```python
for i in range(len(arr)):
    print(i, arr[i])
```

### `enumerate()`로 인덱스와 값 얻기

> 학습일: 2026-09-17

`enumerate()`를 사용하면 인덱스와 값을 함께 얻을 수 있다.

```python
for index, value in enumerate(arr):
    print(index, value)
```

---

## 문자열

### 문자열을 한 글자씩 순회하기

> 학습일: 2026-09-17

문자열을 `for`문으로 순회하면 문자를 한 글자씩 꺼낼 수 있다.

```python
text = "abcd"

for char in text:
    print(char)
```

---

## 리스트

### `append()`로 값 추가하기

> 학습일: 2026-09-17

`append()`는 리스트의 마지막에 새로운 값을 추가한다.

```python
answer = []
answer.append(10)

print(answer)  # [10]
```

### 리스트 컴프리헨션

> 학습일: 2026-09-17

반복문을 이용해 새로운 리스트를 간결하게 만들 수 있다.

```python
numbers = [1, 2, 3]
doubled = [number * 2 for number in numbers]

print(doubled)  # [2, 4, 6]
```

일반 반복문으로 작성하면 다음과 같다.

```python
doubled = []

for number in numbers:
    doubled.append(number * 2)
```

---

## 딕셔너리

### 딕셔너리에서 키로 값 찾기

> 학습일: 2026-09-17

딕셔너리는 `키: 값` 형태로 자료를 저장한다.

```python
key = {
    'w': 1,
    's': -1,
    'd': 10,
    'a': -10
}

print(key['w'])  # 1
print(key['a'])  # -10
```

### `dict()`와 `zip()`으로 딕셔너리 만들기

> 학습일: 2026-09-17

`zip()`으로 묶은 자료를 `dict()`에 전달하면 딕셔너리를 만들 수 있다.

```python
letters = ['w', 's', 'd', 'a']
numbers = [1, -1, 10, -10]

key = dict(zip(letters, numbers))

print(key)
# {'w': 1, 's': -1, 'd': 10, 'a': -10}
```

---

## 내장 함수

### `zip()`으로 같은 위치의 값 묶기

> 학습일: 2026-09-17

`zip()`은 여러 자료에서 같은 위치에 있는 값들을 묶는다.

```python
letters = ['w', 's', 'd', 'a']
numbers = [1, -1, 10, -10]

print(list(zip(letters, numbers)))
# [('w', 1), ('s', -1), ('d', 10), ('a', -10)]
```

### `sum()`으로 합계 구하기

> 학습일: 2026-09-17

`sum()`은 여러 숫자의 합계를 구한다.

```python
numbers = [1, -1, 10]
print(sum(numbers))  # 10
```

### 여러 기능 조합하기

> 학습일: 2026-09-17

```python
def solution(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum(key[char] for char in control)
```

실행 순서:

1. `zip()`으로 문자와 숫자를 묶는다.
2. `dict()`로 문자별 값을 저장한다.
3. `control`에서 문자를 한 글자씩 꺼낸다.
4. 문자에 해당하는 값을 `sum()`으로 모두 더한다.
5. 합계를 `n`에 더한다.

---

## 실수 기록

### 빈 리스트의 존재하지 않는 인덱스에 대입하기

> 기록일: 2026-09-17

빈 리스트에는 `0`번 위치가 아직 없어서 다음 코드는 `IndexError`가 발생한다.

```python
answer = []
answer[0] = 10  # IndexError
```

새로운 값을 넣을 때는 `append()`를 사용한다.

```python
answer = []
answer.append(10)
```

```python
answer[i] = value     # 이미 존재하는 위치의 값을 변경
answer.append(value)  # 리스트 끝에 새로운 값을 추가
```

---

## 문제 풀이 기록 기준

다음에 해당하는 문제를 중심으로 기록한다.

- 새롭게 알게 된 문법이나 함수가 있는 문제
- 틀렸거나 푸는 데 오래 걸린 문제
- 내 풀이보다 더 간단하거나 배울 점이 있는 풀이가 나온 문제
- 나중에 다시 풀어 보고 싶은 문제

쉽게 풀었고 새로운 내용이 없는 문제는 코드만 남기거나 넘어간다.
