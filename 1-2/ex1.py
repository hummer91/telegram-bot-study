# 두 숫자 a와 b를 입력받아, 둘 중 더 큰 숫자를 출력하는 프로그램을 작성하세요.

if __name__ == "__main__":
    import sys
    val_1 = int(sys.argv[1])
    val_2 = int(sys.argv[2])
    if (val_1>val_2):
        print(f"{val_1} is bigger than {val_2}")
    elif (val_1<val_2):
        print(f"{val_2} is bigger than {val_1}")
    else:
        print(f"{val_1} and {val_2} has same value")

