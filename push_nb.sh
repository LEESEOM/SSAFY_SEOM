#!/bin/bash

Git 저장소 경로
git_repo_path="/Users/seom/Desktop/SSAFY_SEOM"

cd "$git_repo_path"
git add .
git commit -m '1'
git push origin main