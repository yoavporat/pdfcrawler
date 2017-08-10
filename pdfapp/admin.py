from django.contrib import admin
import pdfapp.models as models

admin.site.register(models.Doc)
admin.site.register(models.Urls)
