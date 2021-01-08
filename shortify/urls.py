from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='home'),
    path('<str:shorturl>/',views.UrlRedirect,name="urlredirect"),
]