from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from .forms import PostForm
from .models import Post
from .utils import is_positive  # ステップ 4で定義した関数をインポート

from langchain.agents import Tool, initialize_agent, AgentType
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY = settings.OPENAI_API_KEY
OPENAI_API_BASE = settings.OPENAI_API_URL

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
                chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, openai_api_base=OPENAI_API_BASE, model_name='gpt-4o-mini', temperature=0)
                content = f"「{text}」をポジティブな絵文字に変換してください。また、「{text}」は削除してください。"
                messages = [
                    HumanMessage(content=content),
                    ]
                result = chat(messages)
                Post.objects.create(text=result.content)
    else:
        form = PostForm()
    # GETリクエストの場合、またはフォームが表示された直後
    return render(request, 'positive/post_form.html', {'form': form, 'posts': posts})

def failure(request):
    return render(request, 'positive/failure.html')

def post_delete(request, post_id):
    if request.method == 'POST':  # 安全のため、POSTリクエストのみを許可
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect(reverse('home'))  # 削除後はホームページにリダイレクト
    else:
        return HttpResponseRedirect(reverse('home'))  # GETリクエストの場合もホームにリダイレクト

def check_positive(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        is_pos = is_positive(text)
        return JsonResponse({'is_positive': is_pos})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)