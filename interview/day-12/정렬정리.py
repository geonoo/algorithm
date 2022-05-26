from functools import cmp_to_key

students = [("John", 70), ("Mike", 60), ("Andrew", 80)]

#학생의 앞에있는 값인 이름중에 이름의 마지막에 있는 알파벳 순서대로 비교
#따라서 e가 가장 우선순위가 높고 그다음 n 그다음 w 이다.
def comparator_by_name(a, b):
    if a[0][-1] > b[0][-1]:
        return 1
    else:
        return -1

# cmp_to_key()를 사용하여 이름 기준으로 오름차순 정렬
students = [("John", 70), ("Mike", 60), ("Andrew", 80)]
print(sorted(students, key=cmp_to_key(comparator_by_name)))
