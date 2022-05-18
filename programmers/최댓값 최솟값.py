def solution(s):
    lst = sorted(list(map(int, s.split(' '))))
    return str(lst[0])+' '+str(lst[-1])

print(solution("-1 -1"))

"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"