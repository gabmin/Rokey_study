import shutil


shutil.copy("source.txt", "destination.txt")  # 파일 복사
shutil.copy2("source.txt", "destination.txt")  # 메타데이터 유지하며 복사

# 디렉토리 전체 복사
shutil.copytree("source_dir", "destination_dir")

# 파일 및 디렉토리 이동
shutil.move("old_location", "new_location")

# 디렉토리 및 하위 파일 모두 삭제
shutil.rmtree("directory_to_delete")
