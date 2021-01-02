from django.shortcuts import render

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
    return render(request,'core/contact.html',{})