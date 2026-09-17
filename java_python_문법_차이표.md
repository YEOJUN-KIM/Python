# Java ↔ Python 문법 차이표

Java에 익숙한 상태에서 Python을 배울 때 자주 마주치는 문법 차이를 간단히
정리한 표입니다.

  기능             Java                         Python
  ---------------- ---------------------------- -----------------------
  변수 선언        `int a = 10;`                `a = 10`
  문자열           `String name = "Kim";`       `name = "Kim"`
  출력             `System.out.println(a);`     `print(a)`
  조건문           `if (a > 10) { }`            `if a > 10:`
  else if          `else if`                    `elif`
  코드 블록        `{ }`                        들여쓰기
  문장 끝          `;`                          필요 없음
  AND              `&&`                         `and`
  OR               `\|\|`                       `or`
  NOT              `!a`                         `not a`
  같다             `a == b`                     `a == b`
  다르다           `a != b`                     `a != b`
  null             `null`                       `None`
  null 확인        `a == null`                  `a is None`
  null이 아님      `a != null`                  `a is not None`
  boolean          `true / false`               `True / False`
  for              `for (int i=0; i<10; i++)`   `for i in range(10):`
  증가             `i++`                        `i += 1`
  while            `while (a < 10) { }`         `while a < 10:`
  배열/리스트      `int[] a = {1, 2, 3};`       `a = [1, 2, 3]`
  길이             `a.length`                   `len(a)`
  리스트 추가      `list.add(a)`                `list.append(a)`
  함수             `int add(int a, int b)`      `def add(a, b):`
  문자열 변환      `String.valueOf(a)`          `str(a)`
  정수 변환        `Integer.parseInt(a)`        `int(a)`
  문자열 포맷      `"나이: " + age`             `f"나이: {age}"`
  값 비교(객체)    `a.equals(b)`                `a == b`
  동일 객체 확인   `a == b` (참조 비교)         `a is b`
  this             `this`                       `self`

## 자주 쓰는 치환표

``` text
Java        Python
-----------------------
{ }      → 들여쓰기
&&       → and
||       → or
!        → not
null     → None
true     → True
false    → False
else if  → elif
i++      → i += 1
.equals  → ==
```

## if / elif 예시

### Java

``` java
int age = 20;

if (age >= 30) {
    System.out.println("30대 이상");
} else if (age >= 20) {
    System.out.println("20대");
} else {
    System.out.println("10대 이하");
}
```

### Python

``` python
age = 20

if age >= 30:
    print("30대 이상")
elif age >= 20:
    print("20대")
else:
    print("10대 이하")
```

## None 예시

### Java

``` java
String name = null;

if (name == null) {
    System.out.println("이름이 없음");
}
```

### Python

``` python
name = None

if name is None:
    print("이름이 없음")
```

## `==`와 `is`

Python에서는 둘의 의미가 다릅니다.

``` python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True: 값이 같음
print(a is b)  # False: 서로 다른 객체
```

``` python
a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True: 같은 객체를 가리킴
```

-   `==` : 값이 같은지 비교
-   `is` : 동일한 객체인지 비교
-   `None` 확인에는 보통 `is None`, `is not None`을 사용
