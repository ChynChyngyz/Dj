from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    """Text block"""
    headers_text_title = get_object_or_404(TextBlock, identifier='headers_text_title')

    menu_about = get_object_or_404(Navigation, identifier='menu_about')
    menu_services = get_object_or_404(Navigation, identifier='menu_services')
    menu_cases = get_object_or_404(Navigation, identifier='menu_cases')
    menu_price = get_object_or_404(Navigation, identifier='menu_price')
    menu_articles = get_object_or_404(Navigation, identifier='menu_articles')
    menu_rp = get_object_or_404(Navigation, identifier='menu_rp')
    phone_number = get_object_or_404(Navigation, identifier='phone_number')

    promotion_title = get_object_or_404(Promotion, identifier='promotion_title')
    promotion_subtitle = get_object_or_404(Promotion, identifier='promotion_subtitle')
    promotion_phone = get_object_or_404(Promotion, identifier='promotion_phone')
    promotion_button = get_object_or_404(Promotion, identifier='promotion_button')

    case_title = get_object_or_404(Case, identifier='case_title')
    case_shop = get_object_or_404(Case, identifier='case_shop')
    case_years = get_object_or_404(Case, identifier='case_years')
    case_price = get_object_or_404(Case, identifier='case_price')
    case_price_plus = get_object_or_404(Case, identifier='case_price_plus')
    case_text = get_object_or_404(Case, identifier='case_text')
    case_price_second = get_object_or_404(Case, identifier='case_price_second')
    case_price_second_plus = get_object_or_404(Case, identifier='case_price_second_plus')
    case_stock = get_object_or_404(Case, identifier='case_stock')
    case_price_third = get_object_or_404(Case, identifier='case_price_third')
    case_decrease = get_object_or_404(Case, identifier='case_decrease')
    case_check = get_object_or_404(Case, identifier='case_check')

    carousel_title = get_object_or_404(Carousel, identifier='carousel_title')
    carousel_subtitle = get_object_or_404(Carousel, identifier='carousel_subtitle')
    carousel_text = get_object_or_404(Carousel, identifier='carousel_text')
    carousel_price = get_object_or_404(Carousel, identifier='carousel_price')
    """Text block"""

    """Images"""
    logo = get_object_or_404(Image, identifier='logo')

    carousel = get_object_or_404(Image, identifier='carousel')

    photo = get_object_or_404(Image, identifier='photo')
    photo1 = get_object_or_404(Image, identifier='photo1')
    photo2 = get_object_or_404(Image, identifier='photo2')
    photo3 = get_object_or_404(Image, identifier='photo3')
    photo4 = get_object_or_404(Image, identifier='photo4')
    photo5 = get_object_or_404(Image, identifier='photo5')
    photo6 = get_object_or_404(Image, identifier='photo6')
    photo7 = get_object_or_404(Image, identifier='photo7')

    case_logo = get_object_or_404(Image, identifier='case_logo')
    """Images"""
    image = Image.objects.all()

    return render(request, 'web/index.html',
                  {
                      'logo': logo,

                      'headers_text_title': headers_text_title,

                      'image': image,
                      'carousel': carousel,

                      'menu_about': menu_about,
                      'menu_services': menu_services,
                      'menu_cases': menu_cases,
                      'menu_price': menu_price,
                      'menu_articles': menu_articles,
                      'menu_rp': menu_rp,
                      'phone_number': phone_number,

                      'carousel_title': carousel_title,
                      'carousel_subtitle': carousel_subtitle,
                      'carousel_text': carousel_text,
                      'carousel_price': carousel_price,

                      'promotion_title': promotion_title,
                      'promotion_subtitle': promotion_subtitle,
                      'promotion_phone': promotion_phone,
                      'promotion_button': promotion_button,

                      'photo': photo,
                      'photo1': photo1,
                      'photo2': photo2,
                      'photo3': photo3,
                      'photo4': photo4,
                      'photo5': photo5,
                      'photo6': photo6,
                      'photo7': photo7,

                      'case_logo': case_logo,

                      'case_title': case_title,
                      'case_shop': case_shop,
                      'case_years': case_years,
                      'case_price': case_price,
                      'case_price_plus': case_price_plus,
                      'case_text': case_text,
                      'case_price_second': case_price_second,
                      'case_price_second_plus': case_price_second_plus,
                      'case_stock': case_stock,
                      'case_price_third': case_price_third,
                      'case_decrease': case_decrease,
                      'case_check': case_check,
                          }
                  )


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')


def home(request):
    return render(request, 'users/home.html')
