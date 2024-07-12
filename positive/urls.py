from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_create, name='home'),  # ホームページ
    # path('success/', views.success, name='success'),  # 成功ページ
    path('failure/', views.failure, name='failure'),  # 失敗ページ
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),  # 修正: エンティティコードを正常なURL形式に変更
    path('check-positive/', views.check_positive, name='check_positive'),  # 新しく追加
]