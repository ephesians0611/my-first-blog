from django.http import HttpResponse

def post_list(request):
    return HttpResponse("Hello, world! This is the blog homepage.")
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
