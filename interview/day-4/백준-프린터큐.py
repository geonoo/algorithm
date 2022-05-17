from collections import deque

testcase = int(input())
count = []
for i in range(testcase):
    n, check = map(int, input().split())
    # 우선 순위 큐
    priority = deque(map(int, input().split()))

    # 문서가 들어온 순서대로 하기위해
    document = deque(range(n))
    cnt = 0
    while document:
        # 제일 앞에있는 문서의 우선순위가 가장 높으면
        if priority[document[0]] == max(priority):
            # 제일 앞에있는 문서가 check할 값이면
            if document[0] == check:
                cnt+=1
                break
            # 문서가 출력되었으니 해당 순서에있는 우선순위는 가장 낮은 0으로 셋팅
            priority[document[0]] = 0
            # 문서 출력
            document.popleft()
            # 출력한 개수 카운팅
            cnt += 1
        else:
            # 우선순위가 높은게 있기 때문에, 제일 뒤로 보내기기
            document.append(document.popleft())

    count.append(cnt)



print('\n'.join(map(str, count)))

#lst=[int(sys.stdin.readline().strip()) for i in range(n)]


#3 <- 몇 번 테스트 케이스를 반복 할 건지.
#1 0 <- 첫번째가 list의 길이, 두번째가 0번째있는 수가 몇 번째에 큐를 빠져 나오는지
#5 <- list의 원소
#4 2
#1 2 3 4
#6 0
#1 1 9 1 1 1