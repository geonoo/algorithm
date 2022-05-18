import sys

address_cnt = (list(map(int, sys.stdin.readline().strip().split(' '))))
find_cnt = address_cnt[1]
address_cnt = address_cnt[0]

note = {}
for i in range(address_cnt):
    lst = sys.stdin.readline().strip().split(' ')
    note[lst[0]] = lst[1]

find_password = []
for i in range(find_cnt):
    find_password.append(sys.stdin.readline().strip())

for domain in find_password:
    print(note[domain])


# lst1=list(map(int, sys.stdin.readline().strip().split(' ')))

# 비밀번호 최대 20자
# 16 4 -> 총 주소, 비밀번호 찾으려는 주소
# noj.am IU
# acmicpc.net UAENA
# startlink.io THEKINGOD
# google.com ZEZE
# nate.com VOICEMAIL
# naver.com REDQUEEN
# daum.net MODERNTIMES
# utube.com BLACKOUT
# zum.com LASTFANTASY
# dreamwiz.com RAINDROP
# hanyang.ac.kr SOMEDAY
# dhlottery.co.kr BOO
# duksoo.hs.kr HAVANA
# hanyang-u.ms.kr OBLIVIATE
# yd.es.kr LOVEATTACK
# mcc.hanyang.ac.kr ADREAMER
# startlink.io
# acmicpc.net
# noj.am
# mcc.hanyang.ac.kr

#출력
#THEKINGOD
# UAENA
# IU
# ADREAMER