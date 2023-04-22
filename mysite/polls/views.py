from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. b7f57beb is the polls index.")