for i in range(2,10):
    # 짝수만 출력 2의배수,5의 배수만 출력하려면
    if i%2 == 0 or i%5==0:
        print(f"[ {i} 단 ]")
        for j in range(1,10):
            print(f"{i} x {j} = {i*j}")
        print()    
