from django.urls import path
from basic_app import views

app_name = 'basic_app' #app_name keyword'e, hangi uygulaada çalışıyorsan onun ismi string olarak atanır
urlpatterns = [
    path('other/', views.other, name = 'other'),
    path('relative/', views.relative, name = 'relative')
]
