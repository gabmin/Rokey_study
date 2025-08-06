# import json
#
# data = {"name": "홍길동", "age": 25, "city": "서울"}
#
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

import requests

# API 요청
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# JSON 데이터 파싱
data = response.json()

# 결과 출력
print(data)


# 33

# import requests
#
# response = requests.get("https://randomuser.me/api/")
# data = response.json()
#
# user = data["results"][0]
# name = user["name"]
# print(name)


# import matplotlib.pyplot as plt
#
# fruits = ["사과", "바나나", "오렌지", "포도", "수박"]
# sales = [50, 75, 30, 40, 60]
#
# plt.rcParams["font.family"] = "Malgun Gothic"
#
# plt.bar(fruits, sales)
#
# plt.title("과일별 판매량")
# plt.xlabel("과일")
# plt.ylabel("판매량")
#
# plt.show()

# path = "./logfile.log"
# with open(path, "w", encoding="utf-8") as file:
#     file.write("2025-03-30 12:00:01 INFO 서버 시작됨\n")
#     file.write("2025-03-30 12:05:12 ERROR 데이터베이스 연결 실패\n")
#     file.write("2025-03-30 12:10:35 WARNING 응답 속도 저하\n")
#     file.write("2025-03-30 12:15:45 ERROR 사용자 인증 실패\n")
#
#
# log_path = "./logfile.log"
#
# # 추출할 날짜
# target_date = "2025-03-30"
#
# # 로그 필터링
# with open(log_path, "r", encoding="utf-8") as file:
#     for line in file:
#         if line.startswith(target_date):
#             print(line.strip())
