# 기본변수 : 숫자형(정수형,실수형), 문자형, bool형
# 리스트,튜플-수정불가,딕셔너리-key,value
# 여러개 변수를 저장
# a = [1,2,3,4,5]
# b = (1,2,3,4,5)
# a[3] = 1000
# print(a)
# b[3] = 1000
# print(b)

# a = int(input('숫자를 입력하세요. '))
# b = int(input('숫자를 입력하세요. '))
# c = int(input('숫자를 입력하세요. '))
# d = int(input('숫자를 입력하세요. '))

# a = [1,2,3,4,5]
# print(a[10])

# a = [0,0,0,0,0] # 직접생성
# a = [0]*100     # [0]*100 곱으로 생성
# a = [0 for i in range(1,51)] # 리스트내포
# a = [i for i in range(1,51)] # 리스트내포
# print(a)

# [번호,이름,국어,영어,수학]
title = ['번호','이름','국어','영어','수학']
a = [1,'홍길동',100,90,80]
a2 = [2,'유관순',90,80,70]
# 학생이름출력,국어+영어+수학 = 합계점수 출력
# 전개연산자 리스트 : *a = a[0],a[1],a[2],a[3],a[4]
# print("{},{},{},{},{}".format(a[0],a[1],a[2],a[3],a[4]))
print("{}\t{}\t{}\t{}\t{}".format(*title))
print('-'*50)
print("{}\t{}\t{}\t{}\t{}".format(*a))
print("{}\t{}\t{}\t{}\t{}".format(*a2))
# print(*a) # 전개연산자



# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[2]+a[3]+a[4])





# append : 제일뒤에 값을 추가
# a = []
# for i in range(10):
#     a.append(int(input('숫자를 입력하세요.')))

# print(a)    

