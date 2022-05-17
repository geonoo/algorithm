num = 3
result = ('짝수' if num % 2 == 0 else '홀수')
print(f'{num}은 {result}입니다.')

a_list = [1,2,3,4,5]
b_list = [a*2 for a in a_list]
print(b_list)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]


def check_adult(people):
    return ('성인' if people['age'] > 20 else '청소년')

result = list(map(check_adult, people))

# 람다
result = list(map(lambda x: ('성인' if x['age'] > 20 else '청소년'), people))

print(result)


#필터
result = list(filter(lambda x: x['age'] > 20, people))
print(result)

# 인자 정할수있음
def cal(a, b):
    return a + 2 * b

print(cal(3, 5))
print(cal(5, 3))
print(cal(a=3, b=5))
print(cal(b=5, a=3))

# 입력 개수 지정하지 않고
def call_names(*args):
    for name in args:
        print(f'{name}야 밥먹어라~')

call_names('철수','영수','희재')


# 딕셔너리로 바로
def get_kwargs(**kwargs):
    print(kwargs)

get_kwargs(name='bob')
get_kwargs(name='john', age='27')