#문제: 두 숫자를 더하는 함수를 작성하고, 이 함수를 사용해 두 숫자의 합을 출력하세요.
def intsum(int1, int2):
    return int1 + int2

import sys
val_1 = int(sys.argv[1])
val_2 = int(sys.argv[2])

print(intsum(val_1,val_2))