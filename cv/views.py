from django.shortcuts import render
from .models import *
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

def accept(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        education = request.POST.get('education', '')
        university = request.POST.get('university', '')
        experience = request.POST.get('experience', '')
        skills = request.POST.get('skills', '')

        profile = Profile(name=name, email=email, phone=phone, summary=summary, 
                         education=education, university=university, experience=experience, skills=skills)
        profile.save()

    return render(request, 'cv/accept.html')

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cv/resume.html')
    context = {'user_profile': user_profile}
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'utf-8',
    }
    config = pdfkit.configuration(wkhtmltopdf = r'C:\Users\RAHUL\Downloads\wkhtmltox\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

def list(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'cv/list.html', context)
    