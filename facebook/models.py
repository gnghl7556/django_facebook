from django.db import models

# Create your models here.
class Article(models.Model):
    #필드 명
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text =  models.TextField()
    password =  models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True) #현재 날짜를 자동으로 기입
#코멘트 모델
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments')
                                        #만약 article이 삭제되었을 경우 댓글도 사라지게끔 하기위함
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)  # 현재 날짜를 자동으로 기입
    #이 아래부분은 부가적 (해도 안해도 된다.)
    def __str__(self):
        return "글쓴이 : " + self.author + "내용 : "+ self.text