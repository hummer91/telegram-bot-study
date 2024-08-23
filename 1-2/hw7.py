#숙제 6: 중첩 반복문 - 별 찍기
#문제: 사용자로부터 입력받은 숫자만큼의 높이로 삼각형 모양의 별(*)을 출력하세요.

height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    print('*' * i)
