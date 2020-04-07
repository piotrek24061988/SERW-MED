from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .models import News, Emails
from .forms import NewsCreateForm, SendEmailForm


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
        if request.method == 'POST':
            context = SendEmailForm(request.POST)
            if context.is_valid():
                send_mail("Django name:  " + context.cleaned_data['name'] + ", email: " + context.cleaned_data['email'] +
                          ", tytuł: " + context.cleaned_data['title'],
                          context.cleaned_data['content'], 'piotrek24061988@gmail.com',
                          ['piotrek24061988@gmail.com', 'wieslawagorecka1953@gmail.com'], fail_silently=True)
                emails = Emails(name=context.cleaned_data['name'], email=context.cleaned_data['email'],
                                title=context.cleaned_data['title'], content=context.cleaned_data['content'])
                emails.save()
                messages.success(request, 'Twoj email został wysłany')
                return redirect('serw-med-cont')
            else:
                print("form not valid")
        else:
            context = SendEmailForm()
        return render(request, 'contact.html', {'form': context})

    @staticmethod
    def cooperation(request):
        return render(request, 'cooperation.html')

    @staticmethod
    def gallery(request):
        return render(request, 'gallery.html')
