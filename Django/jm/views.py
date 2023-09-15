from django.shortcuts import render

# Create your views here.
def index(request):
    # 게시글 목록 조회해서 템플릿에 전달
    return render(request, 'myapp/index.html')

def new(request):
    return render(request, 'myapp/new.html')

def create(request):
    # 요청에서 데이터 받아와서 DB에 저장하고
    # 목록 조회해서 템플릿에 전달
    return render(request, 'myapp/index.html')

def delete(request):
    # DB에서 삭제하고 목록 조회해서 템플릿에 전달
    return render(request, 'myapp/index.html')