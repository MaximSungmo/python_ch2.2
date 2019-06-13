# 사칙연산
print(2 * 3)
print(2 / 3)
print(2 + 3)
print(2 - 3)


print(2 / 3)
print(2 / 3.0)
print(2.0 / 3.0)

# //(목) ** (지수승)  %(나머지)
print(2//3)
print(2**3)
print(2%3)

# 몫, 나머지 동시에 값을 반환
result, last = divmod(2, 3)
print(result, last)
t = divmod(2, 3)
print(t, type(t))
print(t[0], t[1])

# 연산자 우선순위
print(2+3*4)  # 14
print(-2+3*4)  # 10
print(4/2*2)  # 4

# 결합 순서 주의
print(2 ** 3 ** 4)
print(2 ** (3 ** 4))




