from django.http import HttpResponse
def landing(request):
    return HttpResponse("Welcome to the landing page!")