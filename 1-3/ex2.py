import requests

# BotFather에서 발급받은 API 토큰
bot_token = "7375155298:AAHjmYYV4xPMMQSzHfV0pB-FkJS5qhnMJDg"

# 텔레그램 API URL
url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"

# 메시지를 보낼 대상의 텔레그램 핸들 (예: @myusername)
chat_id = "7027705499"

photo = "AgACAgUAAxkBAAMHZsikXWyouIjmWst6fhL5fphI7-wAArK9MRuzhkFWjufqms8YjPIBAAMCAANzAAM1BA"
# 전송할 메시지
# message = "Hello from my Telegram bot!"

# POST 요청에 보낼 데이터
data = {
    "chat_id": chat_id,
    "photo": photo
}

# POST 요청 보내기
response = requests.post(url, data=data)

# 응답 확인
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message. Status code:", response.status_code)
