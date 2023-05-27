# Logo , Menu
# Hero section
# About
# Services
# contact us
# Login
# card sections
# persentage sections

# Footer


# menus, header, footer, hero section, side bars, carousel, cards, forms


# functions => { create_forms(*args), join_css_html_js(list_code),  }


from Tool.Datas import menus
from random import choice


class Make_web:
    def __init__(self) -> None:
        Logo = ""
        Menu = choice(Menus)
        hero = choice(Hero)
        about = choice(About)
        header = choice(Header)
        footer = choice(Footer)
        carousel = choice(Carousel)
        cards = choice(Cards)
        forms = choice(Forms)
