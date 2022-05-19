from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
# Create your views here.

#显示博客列表
def index(request):
    # return HttpResponse('this is blog!')
    all_articles  = Article.objects.all()  #这里是取所有，如果取某一个article = models.Article.objects.get(pk=1) 
    return render(request, 'index.html', {'articles':all_articles})

#显示单个博客
def articlePage(request, id):  
    article = Article.objects.get(pk = id)
    return render(request, 'article_page.html', {'article':article})


def article_edit_page(request, id):
    # str方法将参数转化为字符串，避免因传递类型差异引起的错误
    # 0代表是新增博客，否则是编辑博客，编辑博客时需要传递博客对象到页面并显示
    if str(id) =='0':
        return render(request, 'article_edit_page.html')   #既然写新博客和编辑都是跳转到同一个页面，而编辑时需要传递参数，
                                                        #而写博客不需要传递参数，为了兼容，我们都传递一个参数，写新博客时传递一个0，以做区别，
    article = Article.objects.get(pk = id)
    return render(request, 'article_edit_page.html',{'article':article})

#编辑单个博客，以及创建新的博客
def article_edit_page_action(request):
    title = request.POST.get('title','默认标题')
    content = request.POST.get('content',"默认内容")
    article_id = request.POST.get('article_id_hidden','0')##隐藏参数，参数是在web中定义  
    print("article_id =",str(article_id ))  
    ##保存数据
    ##如果是0，标记新增，使用create方法，否则使用save方法
    ##新增是返回首页，编辑是返回详情页
    if str(article_id)=='0':
        Article.objects.create(title = title, content=content) #保存数据
        ##数据保存完成，返回首页
        all_articles = Article.objects.all()
        temp = {'articles':all_articles}
        return HttpResponseRedirect(reverse('blog:index_page'),temp)
    article = Article.objects.get(pk = article_id)
    article.title = title    #完成title update
    article.content = content #完成 content update
    article.save()
    return render(request, 'article_page.html',{'article':article})

def articleDelete(request, id):
    article = Article.objects.get(pk = id)
    article.delete()
    articles = Article.objects.all()      #准备返回主页
    return HttpResponseRedirect(reverse('blog:index_page'), {'articles':articles})