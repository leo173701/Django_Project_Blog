from django.urls import path
from . import views
app_name = 'blog' #超级重要
urlpatterns = [
    path('index/',views.index, name = "index_page"),
    path('article/<str:id>',views.articlePage, name = "article_page"),
    path('article/edit/<str:id>',views.article_edit_page, name='article_edit_page'),
    path('article/edit/action/',views.article_edit_page_action, name='article_edit_page_action'),
    path('article/delete/<str:id>',views.articleDelete, name='article_delete')
]