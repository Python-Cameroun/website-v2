from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# HOME VIEW
def home_view(request):
    return render(request,'core/home.html',{})


# ABOUT PAGE VIEW
def about_view(request):
    return render(request,'core/about.html',{})

# COC PAGE VIEW
def coc_view(request):
    return render(request,'core/coc.html',{})

# PYCON PAGE VIEW
def pycon_view(request):
    return render(request,'core/pycon.html',{})


# SUPPORT PAGE VIEW
def support_view(request):
    return render(request,'core/support.html',{})

# CONTACT PAGE VIEW
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # send the email
        try:
            send_mail(
                f'New inquiry [{name}]',
                message,
                email, 
                ['groovyguev@gmail.com'] )
        except BadHeaderError:
            messages.error(request, 'Failed try again.')
            return redirect('contact')
        return render(request,'core/contact.html',{'success':True})
    return render(request,'core/contact.html',{})