from pathlib import Path


# 현재 작업 디렉토리 확인
print(Path.cwd())

path = Path("folder")

# 폴더와 파일 경로 결합
# '/' 연산자는 경로 결합 연산자(pathlib.Path 객체에서 지원)
print(path / "file.txt")


# 디렉토리 및 파일 존재 여부 확인
path = Path("file.txt")
print(path.exists())  # 존재 여부 확인
print(path.is_file())  # 존재 및 파일 여부 확인
print(path.is_dir())  # 디렉토리 여부 확인


# 디렉토리 생성 및 삭제
path = Path("new_folder")
path.mkdir(exist_ok=True)  # 폴더 생성(기존 존재 시, 에러발생 없음)
path.rmdir()  # 폴더 삭제


# 파일 생성 및 삭제
file_path = Path("test.txt")
file_path.touch()  # 빈 파일 생성
file_path.unlink()  # 파일 삭제


# 파일 및 폴더 목록 조회
path = Path(dir)
for item in path.iterdir():
    print(item)


# 파일 확장자 가져오기
path = Path("file")
print(path.suffix)  # 출력: .txt


# 파일 이름 변경 및 이동하기
path = Path("example.txt")
path.touch()  # 파일 생성
destination = Path("new_folder/example.txt")
destination.parent.mkdir(exist_ok=True)  # 대상 폴더 생성
path.rename(destination)
