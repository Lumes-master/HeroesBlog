

from .models import *


menu = [
            {"title_link": 'Home', "url_link": "home"},
                {"title_link": 'Wiki', "url_link": "wiki"},
                {"title_link": 'Add article', "url_link": "add_article"},
                {"title_link": 'Login', "url_link": "login"},
                {"title_link": 'Regisrtration', "url_link": "registration"},
                {"title_link": 'Log out', "url_link": "logout"},
                ]

# class DataMixin:
#
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         # castles=Castle.objects.all()
#         context['menu'] = menu
#         # context["castles"]=castles
#         return context