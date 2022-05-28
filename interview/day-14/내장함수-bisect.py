import bisect

arr1 = [i for i in range(1,100,2)] # [1, 3, 5, 7, 9, 11,.....99]

# 77이 몇 번째 있는지 확인
b = bisect.bisect_left(arr1, 77) # 38
print(b)


# 76이 몇 번째 있는지 확인
# 76은 배열 안에 없어서 커졌을 때의 인덱스를 반환
b = bisect.bisect_left(arr1, 76) # 38
print(b)


# 0이 몇 번 째 있는지 확인
# 0도 마찬가지로 배열안에 없어서 커졌을 때의 인덱스 반환
b = bisect.bisect_left(arr1, 0) # 0
print(b)


# 101은 마지막 인덱스까지 찾았지만 없어서
# 마지막 인덱스 + 1을 해서 반환, 결국 배열의 길이
b = bisect.bisect_left(arr1, 101) # 50
print(b)



# 30~60 사이의 값들
l = bisect.bisect_left(arr1, 30)
r = bisect.bisect_right(arr1, 60)
print(arr1[l:r])