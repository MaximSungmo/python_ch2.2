# set 생성

# dict 만들 시 d = {} 로 만드므로 주의 필요
s = set()

s = {1, 2, 3}


# 기본연산
print(len(s))
print(2 in s)
print(10 not in s)

# 형변환
nums = [1, 2, 3, 4, 2, 5, 6]
s = set(nums)
print(s)
nums = list(s)
print(nums)

# 삽입
s.add(7)
print(s)

# 삭제
s.discard(2)
print(s)

# discard는 없는 애 삭제 요청 시 에러 발생하지 않음
s.discard(2)
print(s)

# remove는 없는 애 삭제를 요청하면 에러 발생함
# s.remove(2)
# print(s)

s.update({2, 7, 8, 9})
print(s)

# 모두 삭제
s.clear()
print(s)


# 수학 집합 관련 객체 함수
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}
print(s1.union(s2))  # 합집합
print(s1.intersection(s2))  # 교집합
print(s1.difference(s2))  # 차집합 s1과 s2 집합 중 s1에만 있는 것
print(s1.symmetric_difference(s2))  # 교집합을 제외한 여집합
print(s1.issuperset(s2))  # 부분집합이냐



