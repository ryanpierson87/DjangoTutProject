from django.shortcuts import render
from .models import Post
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'Auguest 27, 2018'
#     },{
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'Auguest 28, 2018'
#     },{
#         'author': 'Ryan Pierson',
#         'title': 'Blog Post 3',
#         'content': 'Third post content',
#         'date_posted': 'Auguest 29, 2018'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

