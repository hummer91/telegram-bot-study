import requests

# BotFather에서 발급받은 API 토큰
bot_token = "7375155298:AAHjmYYV4xPMMQSzHfV0pB-FkJS5qhnMJDg"

# 텔레그램 API URL
url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

# GET 요청 보내기
response = requests.get(url)

# 응답 확인
# 사진 메시지에서 file_id 추출하기
if response.status_code == 200:
    updates = response.json()
    for update in updates["result"]:
        if "message" in update and "photo" in update["message"]:
            # 가장 큰 사이즈의 photo를 선택 (photo 필드는 리스트)
            file_id = update["message"]["photo"][-1]["file_id"]
            print(f"File ID: {file_id}")
else:
    print("Failed to get updates. Status code:", response.status_code)
