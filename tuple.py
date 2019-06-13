# tuple 생성

t = ()  # 공튜플
t = (1,)  # 괄호 묶음 연산과 다를 바 없으므로 1개짜리 만들 시 꼭 ',' 넣어주면 tuple로 생성 가능

t = (1, 2, 3)
print(t, type(t))

#
# sequence 지원 연산
#

# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])
print(t[::-1])

# 반복
print(t*2)

# 연결
print(t+(12, 13, 14))

# 길이
print(len(t))

# 확인
print(4 in t)
print(4 not in t)

# tuple은 변경 불가능한 immutable
# t[0] = 100

# 여러 개 값의 대입
x, y, z = 10, 20, 30
print(x, y, z)
x, y, z = (10, 20, 30)
print(x, y, z)

# swap
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)


#
# 객체 함수 : 많지 않다(immutable이기 때문에)
#

t= (20, 30, 10, 20)
print(t.index(20))
print(t.count(20))

# 변환
t = (1, 2, 3, 3)
print(t)

# tuple -> set
s = set(t)
print(s, type(s))

# tuple -> list
l = list(t)
print(l, type(l))

# list -> tuple
t = tuple(l)
print(t, type(t))





