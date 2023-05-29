from django.shortcuts import render, redirect
from django.http import JsonResponse
from base.models import Pages
from django.core.serializers import serialize
import json
import requests
import htmlmin
import io
from django.http import FileResponse
from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import random
from .Auto_generate_html import MakeWeb

# Create your views here.
def random_image():
    # URL of website with SVG images
    url = "https://www.google.com/search?q=nocode+svg+images&tbm=isch&ved=2ahUKEwj0j47uy6v-AhVc1HMBHQtXBaYQ2-cCegQIABAA&oq=nocode+svg+images&gs_lcp=CgNpbWcQAzoKCAAQigUQsQMQQzoHCAAQigUQQzoFCAAQgARQrQNYjAtgyw1oAHAAeACAAacCiAHoC5IBBTAuNC40mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=73A6ZLTcItyoz7sPi66VsAo&bih=760&biw=1536&rlz=1C1RXQR_enIN1038IN1038"
    # Make a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = set()
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            image_urls.add(img_url)

    return random.choice(list(image_urls))

def index(request):
    pages = Pages.objects.all()
    return render(request, 'NoCodeBuilderPages/pages.html', { "pages": pages })

def addPage(request):
    return render(request, 'NoCodeBuilderPages/index.html')

def savePage(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        Project_name = request.POST['Project_name']
        page = Pages.objects.create(
            name=Project_name, html=html, css=css, image=random_image())
        page.save()
        # return redirect("http://localhost:3000/")
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]}) 

def editPage(request, id):
    page = Pages.objects.get(pk=id)
    
    return render(request, 'NoCodeBuilderPages/index.html', {"page": page})

def HTML_Edit(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        return render(request, 'NoCodeBuilderPages/htmltoedit.html', {'page': text_input})
    else:
        return render(request, 'NoCodeBuilderPages/get_html.html')
    
def editPageContent(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        page = Pages.objects.get(pk=id)
        page.html = html
        page.css = css
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]})    

def previewPage(request, id):
    page = Pages.objects.get(pk=id)
    return render(request, 'NoCodeBuilderPages/preview.html', {"page": page})


def url(request):
    return render(request, 'common/URL.html')


def Download_file(request):
    url = request.POST.get('text_area')
    response = requests.get(url)
    if request.method == 'POST':
        if 'Download' in request.POST:
            try:
                # Download webpage

                # Parse webpage using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Inline all JS and CSS into HTML
                for script in soup(['script', 'link']):
                    if script.has_attr('src'):
                        # Download and replace external JS and CSS with inline JS and CSS
                        if script.name == 'script':
                            content = requests.get(script['src']).text
                            script.string = content
                            script.attrs = {}
                        elif script.name == 'link' and script['rel'] == ['stylesheet']:
                            content = requests.get(script['href']).text
                            style = soup.new_tag('style', type='text/css')
                            style.string = content
                            script.replace_with(style)

                # Minify HTML
                minified_html = htmlmin.minify(str(soup))

                # Create a file-like buffer to receive the minified HTML data
                buffer = io.BytesIO()
                buffer.write(minified_html.encode('utf-8'))
                buffer.seek(0)

                # Generate a file name for the minified HTML file
                filename = 'minified.html'

                # Create a FileResponse object with the minified HTML data and the specified filename
                response = FileResponse(
                    buffer, as_attachment=True, filename=filename)

                return response
            except:
                return HttpResponse("The code is not open scorce")
    return render(request, 'common/URL.html')


def autogenerate(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        ProjectName = request.POST.get('ProjectName')
        print(query, ProjectName)
        a = MakeWeb(query, ProjectName)
        print("connected..........")
        code = a.create_page()
        print("buffering.....")
        buffer = io.BytesIO()
        buffer.write(code.encode('utf-8'))
        buffer.seek(0)
        # Generate a file name for the minified HTML file
        filename = 'Generated_code.html'

        # Create a FileResponse object with the minified HTML data and the specified filename
        response = FileResponse(
            buffer, as_attachment=True, filename=filename)

        return response
    return render(request, 'common/Autogenerate.html')
 
 
def autogenerate_edit(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        ProjectName = request.POST.get('ProjectName')
        print(query, ProjectName)
        a = MakeWeb(query, ProjectName)
        print("connected..........")
        code = a.create_page()
        return render(request, 'NoCodeBuilderPages/htmltoedit.html', {'page': code})
    return render(request, 'NoCodeBuilderPages/Autogenerate1.html')
 