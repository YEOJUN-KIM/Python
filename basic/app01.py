# 실행 : Ctrl + F5
print("Hello World!")

name = "Alice"

age= 26
print(f"{name}의 나이는 {age}살입니다!")

for a in range(10):
    print(a)

name = None

if name == "Alice":
    print("앨리스입니다.")
elif name is None:
    print("이름이 없습니다.")
else:
    print("다른 사람입니다.")


x= 10 
y= 3.14
boola = True
print(x, type(x), y, type(y), boola, type(boola))

name = "Alice"
Name = "ALICE"

print(f"{name}{Name}{x - y :.3f}")
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)

text = 'Python'
#text[시작부분: 끝나는 부분:간격]
print(text[0])
print(text[1])
print(text[0 : 2])
print(text[2::2])

#함수사용
print(text.upper())
print(text.lower())
text = "hello Python"
print(text.capitalize())
print(text.replace("hello", "bye"))
print(text.split())
print(text.count('o'))
text="   hi    "
print(text)
print(text.strip())

#포맷팅
name = "Alice"
age= 26
print(f"{name}님의 나이는 {age}살입니다!")
