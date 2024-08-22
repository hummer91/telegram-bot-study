# 1부터 20까지의 숫자를 출력하면서, 
# 숫자가 홀수인지 짝수인지 함께 출력하는 프로그램을 작성하세요.

for i in range(1,21):
    if (i%2==0):
        print(f"{i} is even number")
    else :
        print(f"{i} is odd number")