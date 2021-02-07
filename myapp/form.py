from django.forms import ModelForm
from .models import Chapter, File, Subject

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['level','subject','chapter','pdf']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.none()
        self.fields['chapter'].queryset = Chapter.objects.none()
 
        if 'level' in self.data:
            try:
                level_id = int(self.data.get('level'))
                self.fields['subject'].queryset = Subject.objects.filter(level_id=level_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.level.subject_set.order_by('name')

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['chapter'].queryset = Chapter.objects.filter(subject_id=subject_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['chapter'].queryset = self.instance.subject.chapter_set.order_by('name')