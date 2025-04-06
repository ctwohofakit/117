from django.urls import path
from . import views
from .views import Projects_list_view, Update_Project_View, Create_Project_View, Detail_Project_view,Delete_Project_view

urlpatterns =[
    path("",views.Projects_list_view.as_view(), name="list"),
    path("new/",Create_Project_View.as_view(), name="new"), 

    path("<int:pk>/",views.Detail_Project_view.as_view(), name="detail"),
    path("<int:pk>/edit/",views.Update_Project_View.as_view(), name="edit"),
    path("<int:pk>/delete/",views.Delete_Project_view.as_view(), name="delete"),

    path("draft/", views.Draft_Project_View.as_view(), name="draft"),
    path("archive/", views.Archived_Project_View.as_view(), name="archive"),


]