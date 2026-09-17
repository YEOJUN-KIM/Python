# 리스트 - 배열과 동일
fruits = ['사과', '바나나', '복숭아', '망고']
student_scores = [97,98,100,50]
mixed_list = ['사과', 100, True, 3.14, [1,2,3,4]]

print(fruits[-1]) #반대로 간다
print(student_scores[1:3])
print(mixed_list)
print(mixed_list[4][2])

# 요소 추가
fruits.append('용과')
print(fruits)
fruits.remove('바나나')
print(fruits)

#튜플
colors = ('red', 'blue', 'green')
print(colors[1])
#colors[1] = 'yellow'  #튜플은 요소를 변경(수정)할 수 없다
print(colors[1])

#딕셔너리 - 사전 {키 : 값}
student_info =  {
    'name' : '홍길동',
    'age' : 27,
    'school' : '부경대학교'
} 
city_popul =  {
    '서울' : 10000000,
    '부산' : 5000000,
    '창원' : 1200000
} 
print(student_info)
print(city_popul)