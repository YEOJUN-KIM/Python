"""기억해 둘 Python 기초 문법 예제."""


# f-string: 문자열 안에 변수의 값을 넣는다.
name = "Alice"
age = 26

print(f"{name}는 {age}살")


# 문자열 슬라이싱: text[시작 위치:끝 위치:간격]
# 끝 위치의 문자는 포함되지 않는다.
text = "Python"

print(text[0])       # P
print(text[0:2])     # Py
print(text[2::2])    # to
