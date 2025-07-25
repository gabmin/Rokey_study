import re

pattern = r"\w+"
text = "Hello, World!"
print(re.findall(pattern, text))

pattern = r"(ab)+"
text = "ababab"
match = re.match(pattern, text)
print(match.group())


text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"

pattern = r"[a-z0-9@.]+"
data = re.findall(pattern, text)
print(data)

text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"

pattern = r"[\d-]+"
data = re.findall(pattern, text)
print(data)


text = "I love Python. Java is also popular. Python is great for AI."

pattern = r"[^.]*\bPython\b[^.]*\."
data = re.findall(pattern, text, re.DOTALL)
print(data)

text = "상품 코드: A123, B456, C789, 가격: 12000원"
pattern = r"\d+"
data = re.findall(pattern, text)
print(data)


text = "NASA is working on AI projects with IBM and Google."
pattern = r"[A-Z]{2,}"
data = re.findall(pattern, text)
print(data)
