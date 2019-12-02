from django.shortcuts import render
from django.views.generic import View
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from django.http import HttpResponse


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


# @method_decorator(csrf_exempt, name='dispatch')
class SingleView(View):
    def get(self, request):
        print("HELLO")
        return render(request, 'single.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f"{key}: {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class MovieView(View):
    def get(self, request):
        return render(request, 'movie.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')