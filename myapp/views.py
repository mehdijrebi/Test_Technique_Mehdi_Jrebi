from myapp.models import Chapter, File, Subject
from django.db.models.fields import files
import myapp
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .form import FileForm
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy


def index(request):
    return render(request,'index.html')

class pdfList(ListView) :
    model=File
    context_object_name = "files"
    template_name="index.html"

class createFile(CreateView):
    model = File
    form_class = FileForm
    template_name = "createFile.html"
    success_url = reverse_lazy('pdfList')

def load_subjects(request):
    level_id = request.GET.get('level')
    subjects = Subject.objects.filter(level_id=level_id).order_by('name')
    return render(request, 'subjectDropDown.html', {'subjects': subjects})

def load_chapters(request):
    subject_id = request.GET.get('subject')
    chapters = Chapter.objects.filter(subject_id=subject_id).order_by('name')
    return render(request, 'chapterDropDown.html', {'chapters': chapters})
def loadFilesByDate(request):
    date_id = request.GET.get('date')
    files = File.objects.filter(date=date_id)
    return render(request,'filtredList.html',{'files':files})

    

    
