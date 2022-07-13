from django.urls import path
from .views import *


urlpatterns = [
    path('api/menu/', MenuApiView.as_view()),
    path('api/index/', ArticleApiList.as_view(), name='index'),
    path("api/castle/<int:pk>/", CastleApiDetail.as_view(), name='castle'),
    path("api/article/<int:pk>/", ArticleApiDetail.as_view(), name='article'),
    # path("login/", LoginUser.as_view(), name="login"),
    # path('article/<int:pk>/', ArticleDetail.as_view(), name = 'article'),
    # path("wiki/", WikiList.as_view(), name="wiki"),
]
