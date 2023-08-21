from webapps import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.DetailPost.as_view(), name='detail'),
    path('add', views.Addpost.as_view(), name='add'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
