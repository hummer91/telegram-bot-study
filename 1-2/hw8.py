#숙제 7: 구구단 전체 출력
#문제: 2단부터 9단까지의 구구단을 출력하는 프로그램을 작성하세요.

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")