from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_login,name="user_login"),
    path('<int:id>/details',views.details,name="question_details"),
    path('login/',views.index,name="index"),
    path('welcome/',views.welcome,name="user_welcome"),
    path('register/',views.resgister,name="user_register"),
    path('like/',views.likes,name="user_likes"),
    
]