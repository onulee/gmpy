list = ['홍','이','유','김']
print(list)

for i in list:
    print(i,end='')
print("-"*30)
print(*list)   #구조분해할당 

print('[ 학생성적프로그램 ]')
print('-'*60)
title = ['학번','이름','국어','영어','수학','합계','평균','등수']
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*title))
print('-'*60)

# for i,v in enumerate(list):
#     print(i,v)

# for i in list:
#     print(i)

# for i in range(5):
#     print(i)
