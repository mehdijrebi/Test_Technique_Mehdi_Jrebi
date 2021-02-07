import os
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.functional import keep_lazy_text

class Level(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self) :
        return self.name
  
class Subject(models.Model):
    name = models.CharField(max_length=25)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    def __str__(self) :
        return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=25)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True) 
    def __str__(self) :
        return self.name


@keep_lazy_text
def get_valid_filename(s):
    s = force_text(s).strip()
    return s


class CleanFileNameStorage(FileSystemStorage):
       
    def get_valid_name(self, name):
        return get_valid_filename(name)

def content_file_name(instance, filename):
    new_filename=instance.chapter.name
    while os.path.exists(settings.MEDIA_ROOT +"\\" + new_filename + '.' +filename.split('.')[1])==True:
        new_filename = new_filename + ("(1)")
    return  new_filename+ '.'+filename.split('.')[1]
  

class File(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    pdf = models.FileField(upload_to=content_file_name ,storage=CleanFileNameStorage(),null=True)
    def __str__(self) :
        return self.pdf
   
       


