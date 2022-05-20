
def solution(phone_book):
    m = {}
    # 딕셔너리에 휴대폰 번호를 모두 넣는다.
    for i in range(len(phone_book)):
        m[phone_book[i]] = i

    #휴대폰 주소록 리스트 만큼
    for i in range(len(phone_book)):
        #리스트 원소의 str의 인덱스
        for j in range(1,len(phone_book[i])):
            #접두어로 자른게 휴대폰 번호랑 같다면 False
            if phone_book[i][:j] in m:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))

# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false