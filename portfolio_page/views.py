from django.shortcuts import render


def portfo(request):
    return render(request, 'portfolio_page/index.html', {})
