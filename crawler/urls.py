from django.conf.urls import url
from django.contrib import admin

from pdfapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^all/', views.all_docs, name='all_docs'),
    url(r'^doc/(?P<filename>.*)/', views.doc, name='doc'),
    url(r'^urls/', views.urls, name='urls')
]
