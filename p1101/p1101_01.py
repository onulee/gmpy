# 함수,클래스 : 
# 1. 코드의 재사용
# 2. 코드가 간결
# 3. 프로그램, 유지보수 용이함.

# 1명의 학생의 성적을 입력받아, 성적을 출력하시오.
# 학생정보 - 학번,이름, 나이, 주소, 전화번호, 학과, 학년
# 1, 홍길순, 20, 서울, 010, 컴퓨터공학, 1
# 학생성적 - 학번,이름, 국어,영어,수학,합계,평균,등수
# 1,홍길동 100,100,100,300,100,1
title = ['학번','이름','국어','영어','수학','합계','평균','등수']
students = []
total = 0
avg = 0
rank = 0

# 입력부분
for i in range(3):
    stu = []
    for i,v in enumerate(title):
        if i==(len(title)-3): break
        temp = input(f'{v} 입력하세요.>>')
        if i<2:
            stu.append(temp)
        else:
            total += int(temp)   # total = total + int(temp)
            stu.append(int(temp))    
    avg = total/(len(title)-2)
    stu.append(total)
    stu.append(avg)
    stu.append(rank)     # 1명 학생의 성적
    students.append(stu) # 전체 학생의 성적

### 출력부분
print('[ 학생성적프로그램 ]')
print('-'*60)
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*title))
print('-'*60)
for s in students:
    print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(*s))


# total = int(kor)+int(eng)+int(math)
# avg = total/3
# rank = 0
# print(f'{no},{name},{kor},{eng},{math},{total},{avg},{rank}')




