from django.urls import path,include
from moviedb.views import get_movie , post_movie , update_movie 

urlpatterns = [path('get_movie/' ,get_movie),
              path('post_movie/',post_movie ),
              path('update_movie/',update_movie ),
              ]