# 반복문에는 for:회수 ,while:조건에 따라 무한반복
# for문 변수 in 범위(range,list,dict)
# for i in range(10):  #0,1,2,3,....9
#     print(i)

# for i in range(1,11): #1,2,3,4,5,...10
#     print(i)    

# for i in range(1,10+1,3):
#     print(i)

# for i in range(2,100+1,2):
#     print(i)

# alist = [1,2,3,4,5]
# alist = [1,2,3,4,5]
alist = ['홍길동','유관순','이순신']
# for i in alist:
#     print(i)
# for i in range(len(alist)):
#     print(i+1,alist[i])
# enumerate : index,value값을 2개 넘겨줌
# alist = ['홍길동','유관순','이순신']
# for index,value in enumerate(alist):
#     print(index+1,value)
# alist = ['홍길동','유관순','이순신']
# for i in ['홍길동','유관순','이순신']:
#     print(i)

# 랜덤숫자를 1개 생성해서 맞추는 프로그램
import random
alist = []
ran_num = random.randint(1,100) #랜덤숫자
# for i in range(3):
i = 1
while True:  #무한반복
    num = int(input(f'{i}번째 도전 숫자 >> ')) #내가입력한 숫자
    alist.append(num) # list추가 - append, 삭제-pop
    if ran_num > num:
        print('입력한 숫자가 작습니다. 큰수 입력!')
    elif ran_num < num:
        print('입력한 숫자가 큽니다. 작은수 입력!')  
    else:
        print('정답!!')      
        break
    i+=1

print("정답 :",ran_num)
print('입력한 숫자 : ',alist)