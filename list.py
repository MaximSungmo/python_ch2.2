# 리스트 생성

l = [1, 2, 'python']
print(l, type(l))

# indexing
print(l[::-1])
print(l[-3], l[-2], l[-1], l[0], l[1], l[2])

# slicing
print(l[1:3])
print(l[:])
print(l[1:])
print(l[len(l)-1::-1])

# 반복 *
l2 = l * 2
print(l2)

# 연결 +
l3 = l +[3, 4, 5]
print(l3)

# 길이
print(len(l3))

# 확인
print(5 in l3)

# 삭제
print(l3)
del l3[0]
print(l3)

# 변경가능한 시퀀스(mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이싱을 통한 치환
a = [1, 12, 123, 1234]
a[0:2] = [10, 20] # 슬라이싱 후 값 치환 (갯수 동일)
print(a)
a[0:3] = [10, 20] # 슬라이싱 후 값 치환 (갯수 동일하지 않음), 결과적으로 슬라이싱된 구간을 떼어 새롭게 추가된 리스트를 붙인다.
print(a)
a[1:2] = [20]
print(a)

# 슬라이싱을 통한 삭제
a = [1, 12, 123, 1234]
a[1:2] = []
print(a)
# a[:] = []
# print(a)

# 중간
a[1:1] = ['a']
print(a)

# 마지막
a[5:] = [12345]
print(a)

# 처음
a[:0] = [0]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)

#
# 객체함수
#

# 중간 삽입
a = [1, 12, 123, 1234]
a.insert(1, 'a')
print(a)

# 마지막 삽입
a = [1, 12, 123, 1234]
a.append('last')
print(a)

# 처음 삽입
a = [1, 12, 123, 1234]
a.insert(0, 'a')
print(a)

# reverse
a.reverse()
print(a)

# 제거
print(a)
# a.remove(3) # 값으로 제거함, 인덱스로 제거하려면 다른 방식이 필요
print(a)

# 확장
a.extend([-1, -2, -3])
print(a)

# 스택으로 사용하기
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())

# 큐로 사용하기
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))


# sort()
l3 = [1, 5, 2, 3, 40, 9, 8]
print(l3)
l3.sort()
print(l3)

l3.sort(reverse=True)  #역순으로 정렬
print(l3)

l3 = [10, 2, 22, 9, 8, 33, 4, ]
l3.sort(key=int)
print(l3)

# cf. 내장(전역) 함수 sorted
l3 = [10, 2, 22, 9, 8, 33, 4]
l4 = sorted(l3)
print(l4)

l4 = sorted(l3, reverse=True)
print(l4)

l3 = [10, 45, 22, 33, 91, 35, 44]
def f(n):
    return n % 10


l4 = sorted(l3, key=f)
print(l4)















