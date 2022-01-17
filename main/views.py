

from django.http import HttpResponse


def main_index(request):
    return HttpResponse('Salom')