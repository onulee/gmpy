# for, while
# 1-10까지 짝수의 합을 구하시오.
sum = 0
i = 1
while i<=10:
    if i%2==0:
        sum += i
        print(sum)
    i += 1 # 증감식
print(f"합계 : {sum}")    


# sum = 0
# for i in range(1,11):
#     sum += i
# print(f"합계 : {sum}")    