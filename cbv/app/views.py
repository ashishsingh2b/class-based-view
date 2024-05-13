from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def myview(request):
    
    return HttpResponse('<h1>Function based View<h1>')

class Myviews(View):
    name = "Sonam"
    def get(self,request):
        
        #return HttpResponse('<h1>Class based view<h1>')
        return HttpResponse(self.name)
    
class Home(View):
    def get(self,request):
        context= {'msg':'Welcome home'}
        return render (request,'home.html',context)
    