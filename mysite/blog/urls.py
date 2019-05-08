from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new',views.post_new,name='post_new'),
    path('post/edit/<int:pk>/',views.post_edit,name='post_edit'),
    path('post/drafts',views.post_draft,name='post_draft'),
    path('post/drafts/<int:pk>/',views.post_publish,name='post_publish'),
    path('post/delete/<int:pk>/',views.post_delete,name='post_delete'),
    path('register/',views.register,name='register'),
    path('comment/<int:pk>/new',views.comment_new,name='comment_new'),
]
