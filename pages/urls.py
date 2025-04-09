from django.urls import path
from .import views
from .views import AboutPageView, ExpierenceView

urlpatterns=[
    path("", AboutPageView.as_view(), name="about"),
    path("expierence/", ExpierenceView.as_view(), name="expierence"),
    path("contact/", views.contact_view, name="contact"),
]

