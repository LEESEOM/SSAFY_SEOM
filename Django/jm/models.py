from django.db import models

# Create your models here.
class Article(models.Model):
    # 데이터 정의 및 데이터 연결의 역할
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # 매직메서드라서 원래 기본으로는 object어쩌고 되어있는걸 
    # 타이틀 명칭으로 바꿔주는 것!
    def __str__(self):
        return self.title
    # 관리자 페이지에서 제목에 이름 뜨도록 만드는 것!