from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .models import Project, ContactSubmission

def index(request):
    projects = Project.objects.all().order_by('title')
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Save form data to ContactSubmission model
        ContactSubmission.objects.create(
            contact_email=form.cleaned_data['contact_email'],
            contact_phone=form.cleaned_data['contact_phone'],
            project_title=form.cleaned_data['project_title'],
            project_description=form.cleaned_data['project_description']
        )
        return JsonResponse({'status': 'success'})  # Return JSON response

    context = {
        'projects': projects,
        'form': form,
    }
    return render(request, 'core/index.html', context=context)


def success(request):
    return render(request, 'core/success.html')
