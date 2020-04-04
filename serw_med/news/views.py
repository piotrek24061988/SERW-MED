from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .forms import NewsCreateForm


class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'newses'
    ordering = ['-date_posted']
    paginate_by = 10


class UserNewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'newses'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date_posted')


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_single.html'


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'news_create.html'
    form_class = NewsCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'news_create.html'
    form_class = NewsCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = '/news/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SerwMed:
    def __init__(self):
        pass

    @staticmethod
    def about(request):
        return render(request, 'about.html', {'title': 'my about title'})

    @staticmethod
    def contact(request):
        return render(request, 'contact.html')

    @staticmethod
    def cooperation(request):
        return render(request, 'cooperation.html')

    @staticmethod
    def gallery(request):
        return render(request, 'gallery.html')
