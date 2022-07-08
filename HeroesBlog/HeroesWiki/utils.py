

from .models import *


menu = [{"title": "Home", "url_name": "index"},
        {"title": "Wiki", "url_name": "wiki"},
        {"title": "Login", "url_name": "login"}
        ]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        # castles=Castle.objects.all()
        context['menu'] = menu
        # context["castles"]=castles
        return context