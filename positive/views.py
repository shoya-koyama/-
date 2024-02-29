from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
from .models import Post
from .utils import is_positive  # ステップ 4で定義した関数をインポート

def post_create(request):
    posts = Post.objects.all()  # データベースからすべての投稿を取得
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            if is_positive(text):
                Post.objects.create(text=text)  # テキストをデータベースに保存
                # 成功した場合、すべての投稿を含むページを再度表示
                return render(request, 'positive/post_form.html', {'form': PostForm(), 'posts': posts})
            else:
                # テキストがポジティブでない場合
                return render(request, 'positive/failure.html')
    else:
        form = PostForm()
    # GETリクエストの場合、またはフォームが表示された直後
    return render(request, 'positive/post_form.html', {'form': form, 'posts': posts})

# def success(request):
#     return render(request, 'positive/success.html')

def failure(request):
    return render(request, 'positive/failure.html')

def post_delete(request, post_id):
    if request.method == 'POST':  # 安全のため、POSTリクエストのみを許可
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect(reverse('home'))  # 削除後はホームページにリダイレクト
    else:
        return HttpResponseRedirect(reverse('home'))  # GETリクエストの場合もホームにリダイレクト
