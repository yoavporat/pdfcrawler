from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

import PyPDF2
import json

from models import Doc, Urls
import engine


@csrf_exempt
def upload(request):
    if request.method == 'POST' and len(request.FILES) == 1:
        # valid file upload request - create Doc object
        doc_obj, created = Doc.objects.get_or_create(doc_name=request.FILES['file'].name)

        # init PDF reader
        reader = PyPDF2.PdfFileReader(request.FILES['file'])
        num_pages = reader.numPages
        urls = set()

        for i in range(0, num_pages):
            # read page by page to avoid clutter
            page = reader.getPage(0)

            # extract text from PDF
            text = page.extractText()

            # extract URLs from text and merge into previously found urls
            urls |= engine.extract_urls_from_text(text)

        for u in urls:
            url_obj, created = Urls.objects.get_or_create(url=u)
            url_obj.doc.add(doc_obj)

        return HttpResponse(status=200)

    return HttpResponseBadRequest()


def all_docs(request):
    # fetch all Doc objects
    all = Doc.objects.all()
    data = []

    for doc in all:
        # assemble data per Doc object
        doc_data = {
            'id': doc.id,
            'name': doc.doc_name,
            'urls': doc.urls_set.count()
        }
        data.append(doc_data)

    return JsonResponse(data, safe=False)


def doc(request, filename):
    # fetch requested Doc object
    doc_obj = get_object_or_404(Doc, doc_name=filename)

    # reformat data
    data = [u.url for u in doc_obj.urls_set.all()]

    return JsonResponse(data, safe=False)


def urls(request):
    # fetch all URL objects
    all = Urls.objects.all()
    data = []

    for url_obj in all:
        # assemble data per URL object
        url_data = {
            'url': url_obj.url,
            'count': url_obj.doc.count()
        }
        data.append(url_data)

    return JsonResponse(data, safe=False)
