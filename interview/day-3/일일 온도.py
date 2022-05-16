# 매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력

# 제약
# 1 <= temperatures.length <= 10^5 ( 10만 )
# 30 <= temperatures[i] <= 100

# 입력
# [73,74,75,71,69,72,76,73]

# 출력
# [1, 1, 4, 2, 1, 1, 0, 0]


import time


def daily_temperatures1(T):
    t = [0]*len(T)
    count = 0
    # 이중 for 문
    for i in range(len(T)):
        count = 0
        for j in range(i+1,len(T),1):
            # 카운팅 하다가
            count += 1
            # 다음 온도가 클 때
            if T[i] < T[j]:
                t[i] = count
                break
    return t

# 0.00005 sec
T1 = [73,74,75,71,69,72,76,73]

# 리트코드 GoGo


# 10만개
# 4.30319 sec
# Time Limit Exceeded
T2 = [47,34,47,34,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,47,34,47,34,34,...]

# start = time.time()
# print(daily_temperatures1(T1))
# end = time.time()
# print(f"{end - start:.5f} sec")


def daily_temperatures2(T):
    answer = [0]*len(T)

    stack = []
    for i, cur in enumerate(T):
        while stack and T[stack[-1]] < cur:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

# 0.00005 sec
T1 = [73,74,75,71,69,72,76,73]

# 0.00438 sec
T2 = [47,34,47,34,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,...]

# Time Limit Exceeded


start = time.time()
print(daily_temperatures2(T1))
end = time.time()
print(f"{end - start:.5f} sec")