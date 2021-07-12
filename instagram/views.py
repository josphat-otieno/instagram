from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Images, Profile, Comment
from .forms import ImageForm
from django.views import generic
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user =request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = current_user
            image.save()
            return redirect("index")

    else:
        form = ImageForm()
    return render (request, 'new_image.html', {"form":form})

