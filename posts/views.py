from django.shortcuts import HttpResponse, redirect
import datetime
# Create your views here.

a = datetime.datetime.now()


def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')


def redirect_to_github_view(requests):
    if requests.method == 'GET':
        return redirect("https://github.com/klim312")


def hellow_view(request):
    if request.method == 'GET':
        return HttpResponse(f"Hello! Its my project")


def data_view(request):
    if request.method == 'GET':
        return redirect(f"year : {a.year}\n"
                        f"day : {a.day}\n"
                        f"day of the week : {a.weekday()}\n"
                        f"time : {a.time()}\n"
                        )


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse(f"Goodbye user!\n"
                            f"")

