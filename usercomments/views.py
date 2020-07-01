from django.shortcuts import render, redirect
from .models import Comment
from . import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/userprofile/login/')
def comments_list(request):
    comments = Comment.objects.all().order_by('date')
    return render(request, 'usercomments/comments_list.html',{'comments':comments})


def comments_detail(request, slug):
    comment = Comment.objects.get(slug=slug)
    return render(request,'usercomments/comments_detail.html',{'comment':comment})


@login_required(login_url='/userprofile/login/')
def comments_create(request):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('usercomments:list')
    else:
        form = forms.CreateComment()
    return render(request, 'usercomments/comments_create.html', { 'form': form })

