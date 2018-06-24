from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def members(request):
    return render(request, 'blog/members.html')

def studying(request):
    return render(request, 'blog/studying.html')

def login(request):
    return render(request, 'blog/login.html')
