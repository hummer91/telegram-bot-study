# 사용자가 입력한 숫자에 대한 팩토리얼을 계산하는 프로그램을 작성하세요. 
# (예: 5! = 5 x 4 x 3 x 2 x 1)

def facto(intval):
    if intval == 1:
        return 1
    elif intval>1:
        return intval * facto(intval-1)
    
print(f"{facto(3)}")