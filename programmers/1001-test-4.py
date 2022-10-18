def solution(registered_list, new_id):
    registered_list.sort()

    idx = len(new_id)
    for i in range(0, len(new_id)):
        if new_id[i].isdigit():
            idx = i
            break
    new = []
    if idx == len(new_id):
        new.append(new_id)
        new.append('0')
    else:
        new = new_id.split(new_id[idx])
        new[1] = new_id[idx] + new[1]
    num = new_id.lstrip(new[0])

    last = len(registered_list)
    for i in range(0, len(registered_list)):
        if not registered_list[i].startswith(new[0]):
            last = i
            break
    
    while new_id in registered_list[0:last]:
        num = new_id.lstrip(new[0])
        if num.isdigit():
            n = int(num) + 1
        else:
            n = 1
        new_id = new[0]+str(n)
    
    answer = new_id
    return answer




print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
