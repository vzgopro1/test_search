from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def Next(request, post_id):
    try:
        post = Post231.objects.get(id__exact = post_id)

        context = {
            'post': post
        }

        return render(request, 'posts.html', {'Post': post})
    except:
        return HttpResponse('page not found ')

