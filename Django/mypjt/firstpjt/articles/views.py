from django.shortcuts import render

# Create your views here.
# 함수의 모양이 결정되어 있음
# 1. 첫번째 인자로 '요청'객체를 받음
# 2. 반환값으로 '응답'객체를 반환
# render() : 탬플릿을 이용해서 html 생성 및 응답 생성 (그림그리기)
# templates : 알맹이(데이터) 빠진 html, 위치가 정해져 있음 app/templates/ 하위에 작성
# 렌더링에 필요한 데이터는 3번째 인자로 들어옴
# 데이터는 딕셔너리 형태로 들어옴
def hello(request): # hello/ 라는 요청을 처리하는 함수
    # 사용자가 보낸 username을 받아와서 context name에 넣어야함!!
    context = {
        'name' : request.GET.get('username'),
        'fruits' : ['banana', 'apple','kakao']
    }
    return render(request, 'articles/hello.html', context)

def name_form(request): # 이름을 입력할 수 있는 화면을 응답하는 함수
    return render(request,'articles/throw.html' )