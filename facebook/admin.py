from django.contrib import admin

# Register your models here.
#관리자 페이지에도 DB를 보이게 해주세요
from facebook.models import Article
admin.site.register(Article)

from facebook.models import Comment
admin.site.register(Comment)
