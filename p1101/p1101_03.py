from p1101_04 import *

while True:
    print('[ 학생성적 프로그램 ]')
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('0. 프로그램 종료')
    print('-'*30)
    choice = int(input('원하는 번호를 입력하세요.>> '))
    if choice == 1:
        stuInput()  #함수호출
        stuOutput()
    elif choice == 2:
        stuOutput() #함수호출
    elif choice == 0:
        print('프로그램 종료')
        break        
