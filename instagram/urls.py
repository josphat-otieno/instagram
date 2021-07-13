from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import AddCommentView,  UserEditView
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(\d+)/$',views.image_detail,name ='image_detail'),
    url(r'^new/image$', views.new_image, name='new-image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('update_image/<int:image_id>/', views.update_image, name='update_image'),
    path('likeimage/<int:image_id>', views.like_image, name = 'likeImage'),
    path('comment/(<int:image_id>',views.add_comment, name='add_comment'),
    path('search/', views.search, name='search'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('profile/', views.profile, name='profile')

 ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
