from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.forms import *
from django.urls import reverse
from .models import *


def about(request):
    return render(request, 'main/about.html')

def project(request):
    project = Projects.objects.all().order_by("Date")
    category = Category.objects.all()
    p_form = FeedbackForm()

    if 'submit_p_form' in request.POST:
        p_form = FeedbackForm(request.POST)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.project_comment = Projects.objects.get(id=request.POST.get('project_comment_id'))
            instance.save()
            p_form = FeedbackForm()

    context = {
        'project': project,
        'category': category,
        'p_form': p_form,
    }

    return render(request, 'main/project.html', context)


def feedback(request):
    feedback = Feedback.objects.all()

    context = {
        'feedback': feedback,
    }
    return render(request, 'main/feedback.html', context)

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




