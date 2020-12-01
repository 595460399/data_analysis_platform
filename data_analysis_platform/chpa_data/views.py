from django.shortcuts import render


def index(request):
    context = {'data': 'data'}
    return render(request, 'chpa_data/index.html', context)
