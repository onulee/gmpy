title = ['학번','이름','국어','영어','수학','합계','평균','등수']
students = []

# 학생성적입력함수
def stuInput():
    total = 0
    avg = 0
    rank = 0
    print('[ 학생성적 입력 ]')
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

# 학생성적출력함수
def stuOutput():
    print('[ 학생성적 출력 ]')
    ### 출력부분
    print('[ 학생성적프로그램 ]')
    print('-'*60)
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*title))
    print('-'*60)
    for s in students:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(*s))