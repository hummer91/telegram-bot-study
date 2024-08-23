#숙제 5: 단어 뒤집기
#문제: 사용자가 입력한 문자열을 뒤집어서 출력하는 프로그램을 작성하세요. (예: "Python" -> "nohtyP")

word = input("Enter a word: ")
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word
    # print(f"{reversed_word}")

print(f"Reversed word: {reversed_word}")
