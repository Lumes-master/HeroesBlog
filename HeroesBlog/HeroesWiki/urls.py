from django.urls import path
from .views import *


urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path("castle/<slug:castle_slug>/", CastleDetail.as_view(), name= 'castle'),
    path("login/", LoginUser.as_view(), name="login"),
    path('article/<int:pk>/', ArticleDetail.as_view(), name = 'article'),
    path("wiki/", WikiList.as_view(), name="wiki"),
]
