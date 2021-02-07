from django.contrib import admin
from .models import Chapter, File, Level, Subject
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(File)

