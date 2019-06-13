# packing : tuple만 가능하다

t = 10, 20, 30, 'python'   # tuple로 packing된다.
print(t, type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# 에러
# a, b, c = t  # 변수의 갯수가 맞지 않아 에러
# a, b, c, d, e, f = t  # 변수의 갯수가 맞지 않아 에러

# unpacking extended

t = (1, 2, 3, 4, 5)
a, *b = t  # *b 처럼 작성할 경우 여러개의 tuple을 하나에 받도록 하겠다
print(a)
print(b)

*a, b = t
print(a)
print(b)

a, b, *c = t
print(a)
print(b)
print(c)

a, *b, c = t
print(a)
print(b)
print(c)

# cf. 멀티파라미터 받는 함수
def mysum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum

print(mysum(1, 2, 3))
print(mysum(1, 2, 3, 4, 5, 6))
print(mysum(1, 2, 3, 4, 5))



# printf 기능을 하는 함수 구현
def printf(format, *args):
    print(format % args)

printf("name: %s, age : %d", "둘리", 10)
#name : 둘리, age : 10

