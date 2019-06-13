a = 23
print(a,type(a))
print(isinstance(a, int))

# 2진, 10진, 16진, 8진
b = 0b1101 # 8+4+0+1
c = 0o23 # 8*2 + 3
d = 0x23 # 16*2 + 3
print(b, c, d)

# python version 3.x int long이 합쳐졌다.(무한대 표현범위)
e = 2 ** 1024
print(e)
print(type(e))

# 변환함수 2진수, 8진수, 16진수
print(bin(38))
print(oct(38))
print(hex(38))

