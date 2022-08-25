from django.urls import path
from .views import list_blogs, read_blog


urlpatterns = [
    path('', list_blogs),
    path('blog/<int:blog_id>/', read_blog),
]