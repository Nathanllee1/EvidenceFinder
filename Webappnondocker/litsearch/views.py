from django.shortcuts import render
from rest_framework import serializers
from litsearch.classifier import classify


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

    if request.method == 'POST':
        returned = classify(request.POST['text'], request.POST['theme'])
        return render(request, {'highlighted': returned})
