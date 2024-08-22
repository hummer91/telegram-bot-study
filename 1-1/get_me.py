import requests

# BotFather에서 발급받은 API 토큰
bot_token = "7375155298:AAHjmYYV4xPMMQSzHfV0pB-FkJS5qhnMJDg"

# 텔레그램 API URL
url = f"https://api.telegram.org/bot{bot_token}/getMe"

# API 요청 보내기
response = requests.get(url)

# 응답 출력
if response.status_code == 200:
    print("Bot Info:", response.json())
else:
    print("Failed to get bot info. Status code:", response.status_code)
