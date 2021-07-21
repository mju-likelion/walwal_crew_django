from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def adoption(request):
    return render(request, 'adoption.html')

def passage(request):
    return render(request, 'passage.html')

def failure(request):
    return render(request, 'failure.html')