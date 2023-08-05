from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blogapp.models import Post, Comment


# Create your views here.
def myView(request):
    return HttpResponse('Hello World!')

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', { 'posts': posts})

def blog_create(request):
    mypost = Post()
    if request.method == 'POST':
        mypost.title = request.POST['title']
        mypost.content = request.POST['content']
        mypost.Post_Photo = request.POST['post_photo']
        mypost.save()
        return redirect('/blogapp/index/')
    
    return render(
        request,
        'blogapp/blog_create.html'
    )

'''
def edit_blog(request, pk):
    curPost = Post.objects.get(id=pk)
    print(curPost.id)
    if request.method == 'POST':
        curPost.Title = request.POST['Title']
        curPost.Content = request.POST['Content']
        curPost.Post_Photo = request.POST['post_photo']
        curPost.complete = request.POST.get('complete') == "on"
        curPost.save()
        return redirect(curPost)
    return render(
        request,
        'blogapp/blog_edit.html',
        {
            'curPost' : curPost,
        },
    )
'''


def edit_blog(request, pk):
    curPost = Post.objects.get(id=pk)
    if request.method == 'POST':
        curPost.title = request.POST['Title']
        curPost.content = request.POST['Content']
        
        # 파일 업로드 처리
        if 'post_photo' in request.FILES:
            curPost.post_photo = request.FILES['post_photo']
        curPost.save()
        return redirect('main')
    return render(
        request,
        'blogapp/blog_edit.html',
        {
            'curPost': curPost,
        },
    )
    

def delete_blog(request, pk):
    delblog = get_object_or_404(Post, pk=pk)
    delblog.delete()
    return redirect('main')


def comment_blog(request, pk):
    mkcomment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
       # post = request.POST['post']
        mkcomment.content = request.POST['content'] # 폼에서 'content' 필드로 댓글 내용을 전달받음
        mkcomment.author = request.POST['author']
        #mkcomment.comment = request.POST['comment']  # 댓글 객체를 생성하여 저장
        mkcomment.save()
        return redirect('main')


