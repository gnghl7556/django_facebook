from django.shortcuts import render, redirect
from facebook.models import Article, Comment

# Create your views here.

count = 0

def play(request):
    return render(request,'play.html')

def play2(request):
    #무언가 작업

    #ex) newsfeed게시판
    ahtkdgus = '모상현'

    global count
    count = count + 1
    age = 20
    if age > 19:
        status = '성인'
    else:
        status = '미성년자'

    diary = ['치킨','피자','짜장','곰탕','갈비','샌드위치','도넛','라면','파스타']

    return render(request, 'play2.html',{ 'name' : ahtkdgus, 'count':count,'status':status,'diary':diary})

def profile(request):
    return render(request, 'profile.html')

def event(request):

    age=23
    global count
    count=count+1
    message=""

    if count ==7:
        message = '당첨입니다.'
    else:
        message = '꽝..'
    return render(request, 'event.html',{'name' : '모상현', 'count': count,'age':age, 'message': message})
def newsfeed(request):
    #여기서 DB를 불러와서 newsfeed.html에 올리자
    articles = Article.objects.all()
    return render(request, 'newsfeed.html',{'articles': articles})

def detail_feed(request,pk):
    #코멘트 데이터를 받아서 등록
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password']
                    #request.POST는 폼에 기록된 정보를 불러오는 명령어이다.

        )



    return render(request, 'detail_feed.html',{'feed': article})
def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content'],
            password=request.POST['password']
        )
        # 새글 등록 끝
    return render(request, 'new_feed.html')
def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()
        return redirect(f'/feed/{ article.pk }')
    return render(request, 'edit_feed.html', {'feed': article})
def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫페이지로 이동하기
    return render(request, 'remove_feed.html', {'feed': article})
