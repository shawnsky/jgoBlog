from django.shortcuts import render
from blog.models import Article

# Create your views here.
def home(request):
	articles = Article.objects.all()
	return render(request, 'home.html', {'articles': articles})

def article_detail(request, pk):
	article = Article.objects.get(pk=pk)
	return render(request, 'detail.html', {'article': article})
