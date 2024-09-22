from django.urls import path
from . import views

app_name = "management"
urlpatterns = [
    path("",views.index, name="index"),
    path("budget/add",views.budget_add,name="budget_add"),
    path("logs/",views.budget_log,name="budget_log"),
    path("budget/<uuid:id>",views.log_detail,name="log_detail"),
    path("budget/<uuid:id>/update/",views.log_update,name="log_update"),
    path("budget/<uuid:id>/delete/",views.log_delete,name="log_delete"),
]