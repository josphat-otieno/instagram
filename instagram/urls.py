from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import AddCommentView,  UserEditView
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(\d+)/$',views.image_detail,name ='image_detail'),
    # url(r'^image/(\d+)/$', AddCommentView.as_view(), name ='add_comment'),
    url(r'^new/image$', views.new_image, name='new-image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('update_image/<int:image_id>/', views.update_image, name='update_image'),
    path('likeimage/<int:image_id>', views.like_image, name = 'likeImage'),
    path('comment/(<int:image_id>',views.add_comment, name='add_comment'),
    # path('image/<int:pk>/comment',AddCommentView.as_view(), name ='add_comment'),
   path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
#     path('user_profile<int:pk>', ShowProfilePageView.as_view(), name='user_profile')
 ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
