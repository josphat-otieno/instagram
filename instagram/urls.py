from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import AddCommentView
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(\d+)/$',views.image_detail,name ='image_detail'),
    path('<int:pk>/', AddCommentView.as_view(), name ='add_comment'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)