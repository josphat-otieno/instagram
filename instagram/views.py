from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Images, Profile, Comment
from .forms import ImageForm, CommentForm
from django.views import generic
from django.urls import reverse_lazy, reverse
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
        image_likes = get_object_or_404(Images, id=image_id)
        total_likes= image_likes.total_likes()
    except Images.DoesNotExist:
        raise Http404()

    return render(request,"instagram/image.html", {"image":image, "total_like":total_likes})

class AddCommentView(generic.CreateView):
    model =Comment
    template_name = 'add_comment.html'
    fields = '__all__'

# def new_comment(request, image_id):
#     current_user = request.user
#     if request.method == 'POST':
#         comment_form =CommentForm(request.POST, request.FILES)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit = False)
#             comment.profile = current_user
#             comment.save()
#             return redirect("index")

    # else:
    #     comment_form=CommentForm()

    # return render(request, 'instagram/add_comment.html', {"comment_form":comment_form})

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

def LikeView(request, pk):
    image = get_object_or_404(Images, id=request.POST.get('image_id'))
    image.like.add(request.user)
    return HttpResponseRedirect(reverse('image_detail', args=[str(pk)]))

def delete_image(request, image_id):
    item = Images.objects.get(id =image_id)
    if request.method =='POST':
        item.delete()
        return redirect('/')
    return render(request, 'instagram/delete.html', {"item":item})
    # def deleteTask(request, pk):
    # item = Tasks.objects.get(id=pk)
    # if request.method =="POST":
    #     item.delete()
    #     return redirect("/")
    # context = {"item": item}
    
    
    # return render(request, 'tasks/delete.html', context)



# from .forms import CommentForm

# def post_detailview(request, id):
	
#     if request.method == 'POST':
#         coment_form = CommentForm(request.POST or None)
#         if coment_form.is_valid():
#             content = request.POST.get('content')
#             comment = Comment.objects.create(post = post, user = request.user, content = content)
#             comment.save()
#         return redirect(images.get_absolute_url())
#     else:
#         coment_form = CommentForm()
		
#         context ={
#         'comment_form':coment_form
#         }
#         return render(request, 'instagram/detail.html', context)




