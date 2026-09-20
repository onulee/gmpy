import random # 랜덤으로 숫자를 가져옴

num = random.randint(1,10)
a = int(input("숫자를 입력하세요. "))
if num==a:
    print("정답입니다.")
elif num>a:
    print("입력한 숫자보다 큽니다.")    
else:
    print("입력한 숫자보다 작습니다.")    
print("랜덤숫자 : ",num)
# print(random.random())  # 0<= x < 1
# print(random.randint(1,10)) # 1,10사이 정수1개



# a = int(input("숫자입력 : "))

# if a>0:
#     print("양수입니다.")
# elif a==0:
#     print("0입니다.")    
# else:
#     print("음수입니다.")

# if a<100:
#     print("100보다 작은수입니다.")
# else:
#     print("100보다 큰수입니다.")    


# print(10-7)


# 숫자를 입력받아
# 5보다 크고 20보다 작은수만 출력하시오.
# 맞으면 범위 안의 숫자는 출력
# 그렇지 않으면, 범위를 벗어났습니다. 라고 출력하시오
# num = int(input("숫자입력 : "))
# if 5>=num and num<=20: # 5<= num <= 20
#     print(num)
# else:
#     print("범위를 벗어났습니다.")    


# id = input("아이디 입력 : ")  # aaa
# pw = input("패스워드 입력 : ") # 1111

# if id=="aaa" and pw=="1111":
#     print("로그인이 되었습니다.")
# else:
#     print("아이디 또는 패스워드가 일치하지 않습니다.")    

# a = int(input("숫자입력 : "))
# if a>=10:
#     print("10보다 큰수")
# else:
#     print("10보다 작은수")    


# a = input("숫자입력")
# # 조건절
# if a.isdigit(): # 입력한 값이 숫자로 변환이 가능하면 True
#     a = int(a)
# else:
#     print("숫자만 입력이 가능합니다.")  

# print("입력한 타입 : ",type(a))      




# print(1<10)  # True,False  비교연산자 >,<,==,>=,<=
# print(10**2)


# #str : 더하기-연결, 곱하기-반복
# a = int(input("숫자입력 : "))  
# b = int(input("숫자입력 : ")) 
# print(a*b)  #출력 str+int 에러
# # 타입:int, float




