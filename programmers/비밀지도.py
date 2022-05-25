def solution(n, arr1, arr2):
    answer = []
    jido1 = [format(i,'b') for i in arr1]
    jido2 = [format(i,'b') for i in arr2]

    maxLen = len(max(jido1,key=len))
    for i in range(len(jido1)):
        jido1[i] = '0'*(maxLen-len(jido1[i]))+jido1[i]

    maxLen = len(max(jido2, key=len))
    for i in range(len(jido2)):
        jido2[i] = '0'*(maxLen-len(jido2[i]))+jido2[i]

    for i in range(len(jido1)):
        s = ''
        for j in range(len(jido1[i])):
            if 1 <= int(jido1[i][j])+int(jido2[i][j]): s += '#'
            else: s+= ' '
        answer.append(s)

    return answer


def solution2(n, arr1, arr2):
    answer = []
    jido1 = [format(i, 'b') for i in arr1]
    jido2 = [format(i, 'b') for i in arr2]

    jido1.rjust(n, '0')
    jido2.rjust(n, '0')

    for i in range(len(jido1)):
        s = ''
        for j in range(len(jido1[i])):
            if 1 <= int(jido1[i][j]) + int(jido2[i][j]):
                s += '#'
            else:
                s += ' '
        answer.append(s)

    return answer

def solution3(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        arr = str(format(i|j, 'b')).rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(arr)
    return answer

print(solution3(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))

# n	5
# arr1	[9, 20, 28, 18, 11]
# arr2	[30, 1, 21, 17, 28]
# 출력	["#####","# # #", "### #", "# ##", "#####"]