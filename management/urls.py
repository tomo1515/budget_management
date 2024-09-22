from django.urls import path
from . import views

app_name = "management"
urlpatterns = [
    path("",views.index, name="index"),
    path("budget/add",views.budget_add,name="budget_add"),
    path("logs/",views.budget_log,name="budget_log"),
    path("budget/<uuid:id>",views.log_detail,name="log_detail"),
]