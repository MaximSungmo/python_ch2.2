print(~5) # -6,  (5를 비트로 취한 뒤 역을 하고 +1 )
print(~-1) # 0

# << 연산
a = 4
print( a >> 1)
a = 5
print(a >> 1)

a = -4
print(a>>1)

# bit and or exclusive or
print('bit and, or, exclusive or')
a = 3
print(a & 2) # 2  0000 0011 & 0000 0010 ==> 0000 0010
print(a | 8) # 11 0000 0011  |  0000 0100 ==> 0000 0111
print(0x0f ^ 0x06) # 9  0000 1000 ^ 0000 0110 ==> 0000 1001