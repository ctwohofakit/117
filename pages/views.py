from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm
from django.core.mail import send_mail

class AboutPageView(TemplateView):
    template_name="pages/about.html"

# Create your views here.
def testing_view(request):
    return render(request, "pages/test.html" )


def contact_view(request):
    if request.method=='POST':
        #will validat and send email
        form=ContactForm(request.POST)
        if form.is_valid():
            print("valid data")
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            subject=form.cleaned_data["subject"]
            message=form.cleaned_data["message"]

            message_body = (
                f"This is an email from your portfolio\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n"
                f"Message: {message}"
            )
            
            send_mail(
                "Email from Portfolio",
                message_body,
                email,
                ['ctwohofa@gmail.com'],
            )


        else:
            print("Invalid from data")

    else:
        #display the page
        form =ContactForm()
    return render(request,"pages/contact.html",{"form":form})