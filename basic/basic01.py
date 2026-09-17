# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

# 내가한거
def my_solution(n):
    answer = 0
    if n  % 2 ==1 :
        for a in range(n+1) :
            if a % 2 ==1 :
                answer += a
    elif n % 2 == 0 :
        for a in range(n+1) :
            if a % 2 ==0 :
                answer += (a*a)
    return answer
arr = [1,2,3]
print(len(arr))
print(arr[1])

# 모법답안
def best_solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])


#answer = solution("string", 3)
#print(answer)