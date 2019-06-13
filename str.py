# 한 줄 문자열 정의

s = ''
str1 = 'Hello World'
# s, str1 의 타입 확인
print(type(s), type(str1))
# str1이 str의 인스턴스가 맞는 지 확인
print(isinstance(str1, str))

# 여러 줄 문자열
str2= '''abc
1234
가나다라
'''
print(str2)
# 여러 라인으로 스트링을 쓸 수 있는 것이나 스트링을 받아주는 변수가 없으므로 사라질 예정 주석처럼 사용해줘도 무방함.
'''
여기는 주석 입니다. 
여러 라인 주석을 대체할 수 있습니다. 
'''

# escape
print('"Hello\nWorld\nI\nSay\n"')
'''
"Hello
World
I
Say
"
'''
print('Hello\nWorld\nI\nSay\"ㅇㅇㅇ\"')
'''
Hello
World
I
Say"ㅇㅇㅇ"
'''

#
# 문자열 연산
#

# 1. 인덱싱
#       12345 678910
str1 = 'First String'
print(str1[0], str1[1], str1[2])  # F i r
print(str1[-1], str1[-2], str1[-3])  # g n i
print(str1[::1], str1[::-1])  # First String gnirtS tsriF

# 2. Slicing
#       123456 789101112
str2 = 'Second String'
# s[start:stop:step]
print(str2[2:5])  # con
# print(str2[2:len(str2):1])
print(str2[2:])  # cond String
print(str2[2:len(str2):2])  # cn tig


#    012345
s = "Python"
#   -654321
print(s[-1])  # n
# print(s[-2:len(str2):1])
print(s[-2:])  # on, 마지막 2개 문자
# print(s[0:-2:1])
print(s[:-2])  # pyth,  마지막 2개 문자 제외한 전체 문자열

# print(s[::-1])
print(s[::-1])  # nohtyP, reverse
print(s[1::-1])  # yP, 1번 문자열부터 -1하며 끝까지 슬라이싱
print(s[:-3:-1])  # no, 마지막 문자열부터 -3의 위치까지 슬라이싱
print(s[-3::-1])  # htyP, -3번 문자열부터 -1하며 끝까지 슬라이싱

# 연결(+)
print(str1 + ' ' + str2)  # First String Second String
# 리터럴 연결 시 + 생략 가능
str3= '1st' ' ' '2nd'
print(str3)  # 1st 2nd

# 문자열 객체 연결은 문자열끼리만 할 수 있다. 기존에 자바와 같이 스트링 외 다른 타입의 변수와 합칠 경우 오류 발생
name = '둘리'
age = 10
# print(name + age)  예상은 '둘리10' 이지만  실제 동작 시 오류 발생

# 반복(*)
print(str1 * 3) # First StringFirst StringFirst String

# len() 함수
print(len(str1)) #First String 은 12자리

# in, not in 연산
print('F' in str1) # First String, F  ==> True
print('S' not in str1) # First String, S  ==> # False

# str 객체는 immutable이다.
# str1[0] = 'f' 오류 발생! str은 변경 불가능한 객체이다.

# 서식(formatting) = format 함수
print("name:" + name + ", age : " + str(age))
print("name:" + format(name, "s") + ", age : " + format(age,"d"))
print("name: {0}, age : {1}".format(name, age))

# 서식 : tuble을 사용한 방식
f = "name : %s, age: %d"
print(f % (name, age))
print(f % ("또치", 20))

# 서식 : dictinary 사용한 방식
f = "name : %(name)s, age: %(age)d"
print(f % {'name': name, 'age': age})
print(f % {'name': 'may', 'age': 15})


#
# 객체 함수
#

# 1. 대소문자 관련
s = 'i like Python'
print(s.upper())  # I LIKE PYTHON
print(s.lower())  # i like python
print(s.swapcase())  # I LIKE pYTHON
print(s.capitalize())  # I like python
print(s.title())  # I Like Python

# 2. 검색
s = 'I Like Python, I Like Java Also'
print(s.count("Like"))  # Like 라는 단어는 몇개가 있는 지 카운팅
print(s.find('Like'))  # Like 단어 어느 위치부터 시작하는 지 찾기
print(s.find('Like', 5))  # Like 단어가 5번 위치부터 시작해서 어디 위치부터 시작하는 지 찾기
print(s.rfind('Like'))  # 뒤에서 부터 시작해서 처음 나타나는 위치 찾기

# find와 index 차이점 알아보기
# 결론, 찾는 함수가 없는 경우, find는 -1 , index는 exception 발생, find 쓰는 것이 나을 듯
print(s.index("Like"))  # Like 단어 어느 위치부터 시작하는 지 찾기
# print(s.index("JavaScript"))
print(s.rindex("Like"))  # 뒤에서 부터 시작해서 처음 나타나는 위치 찾기

print(s.startswith("I Like"))  # 시작 스트링이 파라미터와 같은가
print(s.startswith("Like", 2))  # 2번 위치에서 시작하는 스트링은 Like 와 같은가
print(s.endswith("Also"))  # 끝 스트링이 파라미터와 같은가
print(s.endswith("Java", 0, 26))  #0부터 26까지 글 중에서 마지막 스트링이 Java와 같은가

# 편집과 치환
s = '   spam and ham         '
print('------' + s.strip() + '-------')  # 양 옆 공백 삭제(trim과 같은 기능)

s = '<><abc><><defg><><>'
print('------' + s.strip('<>') + '-------')  # 양 옆 '< 또는 >' 로 있는 문자 제거 단, <>< 모두 다 삭제되므로 replace 사용
print(s.replace('<>', ''))

# 분리와 결합
s = 'spam and ham'
l = s.split('and')  # and를 사이에 두고 리스트 형태로 문자열 분리

print(l, type(l))

s2 = ':'.join(l)  # 리스트의 각 문자열을 ':' 으로 결합시킴
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':'))
print(s3.split(':', 2))  # 앞에서부터 2개만 ':' 사용해서 쪼개고 뒤에는 쪼개지 않는다.
print(s3.rsplit(':', 2))  # 뒤에서부터 2개만 ':' 사용해서 쪼개고 뒤에는 쪼개지 않는다.


lines = ''' 1st line
2nd line
3rd line
4th line
'''

print(lines.strip().split('\n'))
print(lines.strip().splitlines())

# 판별
print('1234'.isdigit())
print('1234'.isalpha())

print('abcd'.isalpha())
print('abcd'.isdigit())

print('abcd'.isupper())
print('abcd'.islower())

print('       '.isspace())
print('\r\n\t'.isspace())  # 컨트롤 문자도 '' 스페이스로 인식함

# '0' 채우기
print('20'.zfill(5))  # 패딩처럼 자릿수를 맞추기 위해 0으로 채워줌
print('1234'.zfill(5))  # 패딩처럼 자릿수를 맞추기 위해 0으로 채워줌

# 서식 : 객체함수
print('name:{}, age:{}'.format(name, age))
print('name:{0}, age:{1}'.format(name, age))
print('name:{1}, age:{0}'.format(age, name))
print('{:3}의 제곱근은 {:.7}'.format(122, 122**0.5))  # 3자리까지 , 소수점은 7자리까지만 표시되게끔

print('name:{n}, age:{a}'.format_map({'n': '강아지', 'a': '12'}))  # 딕셔너리 타입으로 변수명을 맵으로 받아 셋팅
















