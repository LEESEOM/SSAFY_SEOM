C:\Users\SSAFY\Desktop\SSAFY_SEOM

#!/bin/bash
# 이 스크립트는 현재 디렉터리에서 Git 저장소로 가정합니다.

# Git 저장소 경로
git_repo_path="C:\Users\SSAFY\Desktop\SSAFY_SEOM"

# Git 명령 실행
cd "$git_repo_path"
git pull origin main
git add .
git commit -m '1'
git push origin main

read -p "Press Enter to exit"

# 끝나고 bash 켜서 chomd -x 파일이름
# 본 파일은 위치 바꾸지 말고 바로가기 만들어서 바탕화면에서 쓰거나 하기