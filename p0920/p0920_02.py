import random

# int,float,str,bool
# 리스트,딕셔너리,튜플 - 여러개 저장이 가능한것은 그냥복사안됨.

a = 1
b = a
print(b)
a=100
print(b)

arr1 = [1,2,3]
arr2 = arr1
print(arr2)
arr1[0] = 100
print(arr1)
print(arr2)
arr2 = [*arr1] #구조분해할당




# 1,45까지 랜덤숫자 1개
# arr = random.randint(1,45)
# arr2 = random.sample(range(1,46),k=6)
# print(arr2)
# 1,45
# for i in range(1,46):
#     print(i)

# 타입 : int,float,str,bool - 값 1개만 저장
# [] : 리스트,딕셔너리,튜플 - 값을 여러개 저장,다른타입 함께 저장가능
# [1,2,3,4,5]