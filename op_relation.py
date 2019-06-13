# 복합관계
a= 6
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 객체 비교
print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] < [1, 2, 0])
# print((1, 3, 2) < [1, 2, 0])
# 튜플과 리스트 비교는 불가능하나 list 생성자를 통해 튜플 객체를 넣어주면 리스트로 변환이 가능하다
print(list((1, 3, 2)) < [1, 2, 0])

# 동질성 비교, 동일성 비교
a = 10
b = 20
c = a
d = 10
print('동질성, 동일성 비교 ')
print(a == b)
print(a is b)
print(a is c)
print(a == c)
print(a is d)
print(a == d)

print('리스트 비교')
l1 = [1, 2, 3]
l2 = [1, 2, 3]
# 값은 같으나
print(l1 == l2)
# 참조 위치는 다름
print(l1 is l2)

# 논리의 계산 순서
print([] or 'logical')
print('local' or 'logical')
print('' and 'logical')
print(None and 1)
print(None or [])
print('pk')

s = 'hello world'
# s가 None 이면 출력하지 않고 None 이 아니라면 출력해라
s and print(s)

def f(msg):
    msg and print(msg)

f('helloworld')







