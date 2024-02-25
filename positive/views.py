from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import PostForm
from .models import Post
from .utils import is_positive  # ステップ 4で定義した関数をインポート

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            if is_positive(text):
                Post.objects.create(text=text)
                return redirect('success')
            else:
                return redirect('failure')
    else:
        form = PostForm()
    return render(request, 'positive/post_form.html', {'form': form})

def success(request):
    return render(request, 'positive/success.html')

def failure(request):
    return render(request, 'positive/failure.html')
