from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Images, Profile, Comment
from .forms import ImageForm
from django.views import generic
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

    return render(request,"instagram/image.html", {"image":image,})

class AddCommentView(generic.CreateView):
    model =Comment
    template_name = 'add_comment.html'
    fields = '__all__'
