from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
# Create your views here.
from .utils import DataMixin


class ArticleList(DataMixin, ListView):
    model = Article
    template_name = "HeroesWiki/index.html"
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        context.update(c_def)
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetail(DataMixin, DetailView):
    model = Article
    template_name = "HeroesWiki/article.html"
    context_object_name = 'article'




class CastleDetail(DataMixin, DetailView):
    model = Castle
    template_name = "HeroesWiki/castle.html"
    context_object_name = 'castle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['units'] = self.object.to_castle.all()
        return context


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'HeroesWiki/login.html'

class WikiList(DataMixin, ListView):
    model = Castle
    template_name = 'HeroesWiki/wiki.html'
    context_object_name = 'castles'