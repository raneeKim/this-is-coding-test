# 큰 수의 법칙


# 입력 조건 
# 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다

# 입력 예시
# 5 8 3 
# 2 4 5 4 6

def solution(n, m, k, data):
    answer = 0
    data.sort()
    
    a = int(m / k)
    b = m % k
    answer += (data[-1]) * (m - b)
    answer += (data[-2]) * b
    return int(answer)

solution(5,8,3,[2,4,5,4,6]) # 46
