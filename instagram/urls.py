from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import AddCommentView
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(\d+)/$',views.image_detail,name ='image_detail'),
    url(r'^image/(\d+)/$', AddCommentView.as_view(), name ='add_comment'),
    # url(r'^comment/(\d+)$', views.new_comment, name = 'new_comment'),
    url(r'^new/image$', views.new_image, name='new-image'),
    path('like<int:pk>', views.LikeView, name = 'like_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('update_image/<int:image_id>/', views.update_image, name='update_image'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
