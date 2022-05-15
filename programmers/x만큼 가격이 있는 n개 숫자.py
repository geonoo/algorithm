# 2	5	[2,4,6,8,10]
# 4	3	[4,8,12]
# -4	2	[-4, -8]

def solution(x, n):
    answer = []

    for i in range(x,n*x+x,x):
        answer.append(i)

    return answer

print(solution(2, 5))

def number_generator(x, n):
    return [i*x+x for i in range(n)]
print(number_generator(2, 5))