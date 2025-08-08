import cv2

image = cv2.imread("./ch21/sample.jpg")
re_image = cv2.resize(image, (700, 500))

colored_image = cv2.cvtColor(re_image, cv2.COLOR_BGR2GRAY)

h, w = re_image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 90, 1)
rotated = cv2.warpAffine(colored_image, M, (w, h))

cv2.imshow("image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

mean_lengths = iris.groupby("species")["sepal_length"].mean()

sns.boxplot(x="species", y="sepal_length", data=iris)
plt.show()

import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), "config.ini")

config = configparser.ConfigParser()

if not os.path.exists(config_path):
    print("config.ini 파일이 없습니다. 새로 생성합니다.")
    config["CLASS"] = {"1반": "", "2반": "", "3반": "", "4반": ""}
    with open(config_path, "w", encoding="utf-8") as configfile:
        config.write(configfile)

config.read(config_path, encoding="utf-8")

ban1 = config.get("CLASS", "1반", fallback="")
ban2 = config.get("CLASS", "2반", fallback="")
ban3 = config.get("CLASS", "3반", fallback="")
ban4 = config.get("CLASS", "4반", fallback="")

print("1반:", ban1)
print("2반:", ban2)
print("3반:", ban3)
print("4반:", ban4)


import os
import configparser
import json

config_path = os.path.join(os.path.dirname(__file__), "config.ini")

config = configparser.ConfigParser()
config.read(config_path, encoding="utf-8")

config_dict = {section: dict(config.items(section)) for section in config.sections()}

json_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(config_dict, json_file, ensure_ascii=False, indent=4)


import os
import json

json_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(json_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

print("불러온 데이터:", data)

# 값 개별 접근
print("1반:", data["CLASS"]["1반"])
print("2반:", data["CLASS"]["2반"])
print("3반:", data["CLASS"]["3반"])
print("4반:", data["CLASS"]["4반"])
