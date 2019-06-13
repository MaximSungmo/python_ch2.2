# dict 생성

d = {'basketball' : 5, 'baseball' : 9}  # key 값은 immotable해야함
print(d, type(d))

# 접근
print(d['basketball'])

# 변경 가능
d['valleyball'] = 6
print(d)

# 반복 *, 연결 + 지원하지 않음(sequence형이 아니기 때문에)

#길이
print(len(d))

# in, not in 가능 (key 값으로만)
print('soccer' in d)
print('baseball' in d)
print('soccer' not in d)


#
# 다양한 dict 객체 생성 방법
#

# 1. literal
d = {}
print(type(d))

# 2. dict() 사용하는 방법 1
d = dict()
print(type(d))

# 3. dict() 사용하는 방법 2 ( = 표현으로)
d = dict(one=1, two=2, three=3)
print(d, type(d))

# 4. dict() 사용하는 방법 3 (리스트와 튜플로)
d = dict([('one', 1), ('two', 2), ('three', 3)])
print(d)

# 5. dict() 사용하는 방법 4 - zip 사용하는 방법
keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)

# 다양한 key 타입(immotable타입만 가능하다)
d = {}
d[True] = 'true'
d[10] = '10'
d['twenty'] = 20
d[(1, 2, 3)] = 6
print(d)

# key 객체
keys = d.keys()
print(keys, type(keys))
for key in keys:
    print("{0}:{1}".format(key, d[key]))

# values 개체
values = d.values()
print(values, type(values))

# items 객체
# [(key1, value1), (key2, value2) ...]
items = d.items()
print(items, type(items))


# 딕셔너리 객체는 자바에서와 마찬가지로 reference를 반환하여 주므로 만일 주소값이 아닌 새로운 객체로 만들고 싶은 경우에는 copy() 함수로 해야함
phone = {
    '둘리': '000-0000-0000',
    '마이콜': '000-0000-0001',
    '또치': '000-0000-0002'
}
p = phone
print(p)
print(phone)
p['도우너'] = '222-2222-2222'
print(p)
print(phone)

p2 = phone.copy()
print(p2)
print(phone)
p2['도우너1'] = '11222-2222-2222'
print(p2, '카피 객체임')
print(phone)

# get() 함수
# 만일 없는 key 값을 넣어줄 경우 get을 사용하는 경우 none, 키 값 인덱싱을 이용하면 exception
print(phone.get('도우너1'))
# exception 발생
# print(phone['도우너1'])


# setdefault 디폴트값이 입력되면 새 값을 넣어줌
phone.setdefault('도우너1','20202020')
print(phone['도우너1'])
print(phone)

# 삭제와 동시에 value 가져오기
number = phone.pop('도우너1')
print(number)
print(phone)

# popitem 마지막 key, value 제거하면서 값을 가져옴
item = phone.popitem()
print(item)
print(phone)

# 업데이트 (중복 값은 업데이트 진행하고 없는 값은 새롭게 업데이트)
phone.update({
    '도우넛': '22222222222',
    '또치' : '000-0000-0003'
})
print(phone)

# 모두 삭제
phone.clear()
print(phone)

