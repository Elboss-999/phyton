from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post,Category
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class CategoryPageListView(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Post.objects.filter(category=category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        return context
    
class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
        categories = Category.objects.all()
        data = []
        for category in categories:
            posts = Post.objects.filter(category=category).all()
            data.append({'category' : category, 'post_len': len(posts)})
        context['post_lens'] = data
        return context    