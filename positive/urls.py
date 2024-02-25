from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_create, name='home'),  # ホームページ
    path('success/', views.success, name='success'),  # 成功ページ
    path('failure/', views.failure, name='failure'),  # 失敗ページ
]
