from django.urls import path
from .import views
from .views import AboutPageView

urlpatterns=[
    path("", AboutPageView.as_view(), name="about"),
    path("contact/", views.contact_view, name="contact"),
]

