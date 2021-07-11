from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Images, Profile, Comment

# Create your views here.
def index(request):
    name = 'instagram app'
    images = Images.objects.all()
    comments = Comment.objects.all()
    return render(request, 'instagram/index.html', {"name":name, "images":images, "comments":comments})

def image_detail(request, image_id):
    try:
        image = Images.objects.get(id = image_id)
    except Images.DoesNotExist:
        raise Http404()

    return render(request,"instagram/image.html", {"image":image})
