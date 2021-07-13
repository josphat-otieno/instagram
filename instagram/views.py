from django.contrib.messages import success
from django.core.checks import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Images, Profile, Comment
from .forms import EditProfileForm, ImageForm, CommentForm, ProfileUpdateForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    name = 'instagram app'
    images = Images.objects.all()
    comments = Comment.objects.all()
    
    return render(request, 'instagram/index.html', {"name":name, "images":images, "comments":comments})

def image_detail(request, image_id):
    try:
        image = Images.objects.get(id = image_id)
        image_likes = image.like.count()
        
    except Images.DoesNotExist:
        raise Http404()

    return render(request,"instagram/image.html", {"image":image, "image_likes":image_likes})

class AddCommentView(generic.CreateView):
    model =Comment
    template_name = 'add_comment.html'
    fields = '__all__'

def like_image(request, image_id):
    image = Images.objects.get(id =image_id)
    image.like.add(request.user)
    image.save()
    return HttpResponseRedirect(reverse('image_detail', args=[str(image_id)]))


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


def delete_image(request, image_id):
    item = Images.objects.get(id =image_id)
    if request.method =='POST':
        item.delete()
        return redirect('/')
    return render(request, 'instagram/delete.html', {"item":item})
   

def update_image(request, image_id):
    image = Images.objects.get(id=image_id)
    update_form = ImageForm(instance=image)
    context = {"update_form": update_form}
    if request.method =="POST":
        update_form = ImageForm(request.POST, instance = image)
        if update_form.is_valid():
            update_form.save()
            return redirect("/")

    return render (request, 'instagram/update_image.html', context)
 

def search(request):
  if 'user' in request.GET and request.GET['user']:
    search_term = request.GET.get('user')
    searched_users = Profile.search_profile(search_term)
    return render(request, 'instagram/search.html', {'users':searched_users})

  else: 
    return render(request, 'instagram/search.html')
    
class AddComment(CreateView):
    model = Comment
    template_name = 'add_commnent.html'
    fields = ['comments']

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name='django_registration/edit_profile.html'
    success_url =reverse_lazy('index')

    def get_object(self):
        return self.request.user

def add_comment(request, image_id):
    image = get_object_or_404(Images, id=image_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES, instance=image)
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            comments.image = image
            comments.user = request.user.profile
            
            return redirect('index')
    else:
        comment_form = CommentForm()
    
    return render(request, 'instagram/add_comment.html',{"comment_form":comment_form, "image":image})

def profile(request):
    if request.method == 'POST':
        user_form=EditProfileForm(request.POST, instance =request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, f'Your profile was updated successfuly')
            return redirect('profile')
    else:
        user_form=EditProfileForm(instance =request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {"user_form":user_form, "profile_form":profile_form}
        return render(request, 'django_registration/user_profile.html', context)



    







