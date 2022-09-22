def solution(n, words):
    answer = [0,0]
    temp = []
    cycle = 1
    step = 0
    for i in range(0,len(words)):
        step += 1
        if step % n == 0:
            step = n
        if step > n:
            step = 1
            cycle += 1

        if words[i] in temp:
            answer[0] = step
            answer[1] = cycle
            break
        temp.append(words[i])

        if len(words)-1 != i and (words[i][-1] != words[i+1][0]):
            step += 1
            if step % n == 0:
                step = n
            if step > n:
                step = 1
                cycle += 1
            answer[0] = step
            answer[1] = cycle
            break

    return answer

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# 3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
# 5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
# 2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]