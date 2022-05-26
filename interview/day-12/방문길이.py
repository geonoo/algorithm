def solution(dirs):
    s = {'U':(1,0),'D':(-1,0),'L':(0,-1),'R':(0,1)}
    visited = set()
    x, y  = 0, 0
    for d in dirs:
        nx, ny = x+s[d][0], y+s[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny))
            visited.add((nx, ny, x, y))
            x,y = nx,ny
    return len(visited)//2



print(solution("LULLLLLLU"))
# "ULURRDLLU"	7