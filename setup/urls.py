
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def test(request):
    return HttpResponse("teste")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    path('post/', include("posts.urls")),
]
