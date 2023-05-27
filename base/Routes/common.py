from django.shortcuts import render, HttpResponse
from .NoCodeAutomate.testing import Nocode_test

def home(request):
    return render(request,'common/index.html')

def blog(request):
    return render(request,'common/blog-single.html')

def automation(request):
    if request.method == 'POST':
        name = request.POST.get('text_area')
        print(name)
        a=Nocode_test()
        a.Make_test(string=str(name))
        my_string = name+"\nCode Compilled sucessfully...."
        response = HttpResponse(my_string, content_type='text/plain')
        return response
    else:
        return render(request,'common/Automation.html')

def compiler(request):
    return render(request,'common/compiler.html')