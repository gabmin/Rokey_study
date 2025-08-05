import os

# 현재 작업 디렉토리 확인
print(os.getcwd())

# 작업 디렉토리 변경
os.chdir("./ch22/os_module")

# 디렉토리 및 파일 목록 조회
print(os.listdir("."))

# 디렉토리 생성
os.mkdir("test_dir")

# 디렉토리 삭제
os.rmdir("test_dir")

# 파일 존재 여부 확인
os.path.exists("test.txt")

# 경로 합치기
print(os.path.join("folder", "file.txt"))

# 파일명만 추출
print(os.path.basename("folder/file.txt"))

# 디렉토리 경로 추출
print(os.path.dirname("folder/file.txt"))
