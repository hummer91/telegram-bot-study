# 주어진 리스트에서 가장 큰 숫자를 찾는 프로그램을 작성하세요. (반복문을 사용해 직접 찾기)

numbers = [3, 41, 12, 9, 74, 15]
max = 0
for number in numbers:
    if max < number :
        max = number

print(f"{max} is largerst in list")