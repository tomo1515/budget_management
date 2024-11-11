from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name="signup"),
    path('my_page/<int:pk>/',views.my_page,name='my_page'),
    #path('signup_done/',views.signup_done,name="signup_done"),
]