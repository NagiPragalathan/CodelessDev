from .Tool.Html_Datas.Datas import *
from .Tool.Html_Datas.base import *
from random import choice
import random
from bs4 import BeautifulSoup
import requests
from googlesearch import search


def get_image_url(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = set()
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            image_urls.add(img_url)
    return list(image_urls)[0]


def listof_get_image_url(keyword, length):
    url = f"https://www.google.com/search?q={keyword}&tbm=isch"

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = set()
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            image_urls.add(img_url)
    return list(image_urls)[:length]


class MakeWeb:
    def __init__(self, query, ProjectName, TitleOftheDocument=False):
        self.Query = query
        self.Theme = ProjectName
        self.ProjectName = ProjectName
        self.DocTitle = TitleOftheDocument or ProjectName
        self.Logo = ""
        self.Menu = choice(Menus)
        self.hero = choice(Hero)
        self.about = choice(About)
        self.footer = choice(Footer)
        self.cards = choice(Cards)
        print("Initialize.....")

    def create_page(self):
        self.code = ''
        self.code += self.add_section(self.Tailwin_Operation(self.Menu))
        self.code += self.add_section(self.Tailwin_Operation(self.hero))
        self.code += self.add_section(self.Tailwin_Operation(self.about))
        self.code += self.add_section(self.Tailwin_Operation(self.cards))
        self.code += self.add_section(self.Tailwin_Operation(self.footer))
        Common_code = self.BaseCode(self.DocTitle, self.code)
        return self.change_Text(Common_code)

    def add_section(self, partOfcode):
        return f"<section>{partOfcode}</section>"

    def BaseCode(self, title, body):
        BaseCode = base_code
        Icon = f"{get_image_url(self.Theme)}".join(BaseCode.split('{-_-}'))
        Title = f"{title}".join(Icon.split('~~~'))
        Body = f"{body}".join(Title.split('~!~'))
        return Body

    def Tailwin_Operation(self, html):
        Colored_html = self.Tailwin_Random_Color_changer(html)
        Image_Changed = self.change_images(Colored_html)
        return Image_Changed

    def Tailwin_Random_Color_changer(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        def random_color_class(prefix):
            colors = ['red', 'orange', 'yellow', 'green',
                      'teal', 'blue', 'indigo', 'purple', 'pink']
            color = random.choice(colors)
            shades = ['100', '200', '300', '400',
                      '500', '600', '700', '800', '900']
            shade = random.choice(shades)
            return f'{prefix}-{color}-{shade}'

        try:
            for elem in soup.find_all(class_=lambda c: c.startswith('bg-') or c.startswith('text-')):
                prefix = elem['class'][0].split('-')[0]
                elem['class'] = [random_color_class(prefix)]
        except:
            pass

        return soup.prettify()

    def change_images(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        try:
            for img in soup.find_all('img'):
                img['src'] = choice(listof_get_image_url(
                    self.Theme, random.choice([10, 15, 20])))
        except:
            pass

        return soup.prettify()

    def Fetch_the_Para_Content(self, query, num_results):
        search_urls = list(search(query, num_results=6))
        extracted_content = []
        try:
            for url in search_urls:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                paragraphs = soup.find_all('p')
                for i in range(min(num_results, len(paragraphs))):
                    extracted_content.append(paragraphs[i].text.strip() + " ")
                print(f"Content from {url}: {extracted_content}\n")
        except:
            print("Error occurred while fetching Content...")

        return extracted_content

    def Fetch_the_HTag_Content(self, query, num_results, find_element):
        search_urls = list(search(query, num_results=3))
        extracted_content = []
        try:
            for url in search_urls:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                elements = soup.find_all(find_element)
                for i in range(min(num_results, len(elements))):
                    extracted_content.append(elements[i].text.strip() + " ")
                    print(extracted_content)
        except:
            print("Error occurred while fetching Content...")
        return extracted_content

    def change_Text(self, html_doc):
        H_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        soup = BeautifulSoup(html_doc, "html.parser")
        p_tags = soup.find_all("p")
        content = self.Fetch_the_Para_Content(self.Theme, len(p_tags))
        try:
            for i, p_tag in enumerate(p_tags):
                p_tag.string = content[i][0:len(p_tag.text)]
        except:
            print("Error occurred in Text.....")

        return str(soup)
