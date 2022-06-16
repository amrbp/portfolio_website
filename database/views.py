from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.forms import ContactForm
from django.urls import reverse
from .models import Contact,Projects,Category


def about(request):
    return render(request, 'main/about.html')

def project(request):
    project = Projects.objects.all()
    category = Category.objects.all()
    
    context = {
        'project' : project,
        'category' : category,
    }

    return render(request, 'main/project.html', context)

def feedback(request):
    contact = Contact.objects.all()

    context = {
        'contact' : contact
    }
    return render(request, 'main/feedback.html',context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form= ContactForm()
        return HttpResponseRedirect(reverse('feedback'))
    
    context={
        'form' : form ,
    }

    return render(request, 'main/contact.html', context)




