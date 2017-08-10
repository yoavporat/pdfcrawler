from django.db import models


class Doc(models.Model):
    doc_name = models.CharField(max_length=50)

    def __str__(self):
        return self.doc_name


class Urls(models.Model):
    url = models.URLField()
    doc = models.ManyToManyField(Doc)
    alive = models.BooleanField()

    def __str__(self):
        return self.url

